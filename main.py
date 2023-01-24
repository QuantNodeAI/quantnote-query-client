import os

import dotenv

from client.query_api_client import HelixirQueryApi

dotenv.load_dotenv(".env")
if __name__ == '__main__':
    AUTH_TOKEN = os.getenv("AUTH_TOKEN")
    client = HelixirQueryApi(auth_token=AUTH_TOKEN)
    query = """SELECT *
    FROM studies.helixir.events
    WHERE event_type = 'listing'
      and date_time >= now()
    ORDER BY date_time
    limit 5;"""
    response = client.get_data_response(query)
    print(response.dtypes)
    print(response)
