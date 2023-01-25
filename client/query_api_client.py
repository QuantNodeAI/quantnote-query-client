import logging
import time
from typing import Optional

import pandas as pd
import requests
from json import dumps
from client.response_model import QueryResponse
from tqdm.auto import trange

client_logger = logging.getLogger("query_api")


class HelixirQueryApi:
    DEFAULT_API_SERVER = "https://auth.helixir.ai/api"
    API_VERSION = "v1"
    APPLICATION_NAME = "HelixirDefaultClient"
    DEFAULT_WAIT_TIME = 0.5

    def __init__(self, auth_token: str, api_server: str = DEFAULT_API_SERVER, api_version: str = API_VERSION,
                 timeout: float = 300):
        self.auth_token = auth_token
        self.headers = {
            "Content-Type": "application/json",
            "x-helixir-api-key": self.auth_token,
            "User-Agent": self.APPLICATION_NAME
        }
        self.api_server = "{api_server}/{version}/queries".format(api_server=api_server, version=api_version)

        self._session = requests.Session()
        self._session.headers.update(self.headers)
        self.timeout = timeout

    def _handle_response(self, query: str, priority: int = 200) -> Optional[QueryResponse]:
        # First of all, query has to be sent as post method
        body = {
            "query": query,
            "priority": priority,
        }

        response = self._session.post(url=self.api_server, data=dumps(body))
        response.raise_for_status()
        response_data = response.json()

        if response_data == "" or response_data is None:
            client_logger.warning("[HelixirQueryApi._handle_response] post -> desired data are empty.")
            return None

        resp = QueryResponse.from_json(response_data)
        get_url = "{url}/{query_id}".format(url=self.api_server, query_id=resp.id)
        max_iteration = int(self.timeout * (1 / self.DEFAULT_WAIT_TIME))
        for i in trange(max_iteration, leave=False, desc="Waiting for response till limit"):
            response = self._session.get(url=get_url)
            response_data = response.json()
            response.raise_for_status()
            if response_data == "" or response_data is None:
                client_logger.warning("[HelixirQueryApi._handle_response] get -> desired data are empty.")
                return None

            resp = QueryResponse.from_json(response_data)
            if resp.loading:
                time.sleep(self.DEFAULT_WAIT_TIME)
            elif resp.error != "":
                client_logger.error("[HelixirQueryApi._handle_response] get -> error: {}".format(resp.error))
                break
            else:
                break

        return resp

    def get_raw_response(self, query: str) -> Optional[QueryResponse]:
        response = self._handle_response(query)
        return response

    def get_data_response(self, query: str) -> Optional[pd.DataFrame]:
        response = self._handle_response(query)
        if response is None or response.data is None:
            return None

        data = pd.DataFrame(
            [r for r in response.data.rows]
        )

        return data
