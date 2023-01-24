import datetime
import json


class Column:
    def __init__(self, friendly_name: str, name: str, col_type: str):
        self.friendly_name = friendly_name
        self.name = name
        self.type = col_type

    def __iter__(self):
        """
        Iterator for object.
        """
        yield from {
            "friendly_name": self.friendly_name,
            "name": self.name,
            "type": self.type,
        }.items()

    def __str__(self):
        """
        String representation of the object.
        """
        return json.dumps(self.to_json(), default=str)

    def __repr__(self):
        """
        Default representation of the object.
        """
        return self.__str__()

    def to_json(self):
        """
        Parse object to the JSON type dictionary.
        """
        to_return = {"friendly_name": self.friendly_name,
                     "name": self.name,
                     "type": self.type}

        return to_return

    @staticmethod
    def from_json(json_dict):
        fr_name, name, col_type = "", "", ""
        if 'friendly_name' in json_dict.keys():
            fr_name = json_dict['friendly_name']
        if 'name' in json_dict.keys():
            name = json_dict['name']
        if 'type' in json_dict.keys():
            col_type = json_dict['type']

        return Column(fr_name, name, col_type)


class Data:
    def __init__(self, columns: list[Column], rows: []):
        self.columns = columns
        self.rows = rows

    def __iter__(self):
        """
        Iterator for object.
        """
        yield from {
            "columns": self.columns,
            "rows": self.rows,
        }.items()

    def __str__(self):
        """
        String representation of the object.
        """
        return json.dumps(self.to_json(), default=str)

    def __repr__(self):
        """
        Default representation of the object.
        """
        return self.__str__()

    def to_json(self):
        """
        Parse object to the JSON type dictionary.
        """
        to_return = {"rows": self.rows}
        columns = []
        for c in self.columns:
            columns.append(c.to_json())

        to_return["columns"] = columns

        return to_return

    @staticmethod
    def from_json(json_dict):
        if 'columns' not in json_dict.keys() or json_dict["columns"] is None:
            return None

        results = json_dict["columns"]
        columns = []
        for b in results:
            columns.append(Column.from_json(b))

        rows = []
        if 'rows' in json_dict.keys():
            rows = json_dict['rows']

        return Data(columns, rows)


class QueryResponse:
    def __init__(self, query_id: str, data: Data, query: str, duration: int, loading: bool, queue: int, error: str,
                 created_at: datetime.datetime, updated_at: datetime.datetime):
        self.id = query_id
        self.data = data
        self.query = query
        self.duration = duration
        self.loading = loading
        self.queue = queue
        self.error = error
        self.created_at = created_at
        self.updated_at = updated_at

    def __iter__(self):
        """
        Iterator for object.
        """
        yield from {
            "id": self.id,
            "data": self.data,
            "query": self.query,
            "duration": self.duration,
            "loading": self.loading,
            "queue": self.queue,
            "error": self.error,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }.items()

    def __str__(self):
        """
        String representation of the object.
        """
        return json.dumps(self.to_json(), default=str)

    def __repr__(self):
        """
        Default representation of the object.
        """
        return self.__str__()

    def to_json(self):
        """
        Parse object to the JSON type dictionary.
        """
        to_return = {"id": self.id,
                     "data": self.data.to_json(),
                     "query": self.query,
                     "duration": self.duration,
                     "loading": self.loading,
                     "queue": self.queue,
                     "error": self.error,
                     "created_at": self.created_at,
                     "updated_at": self.updated_at}

        return to_return

    @staticmethod
    def from_json(json_dict: dict):
        query_id, query, error = "", "", ""
        data = None
        duration, queue = 0, 0
        loading = False
        created_at, updated_at = datetime.datetime.utcnow(), datetime.datetime.utcnow()

        if 'id' in json_dict.keys():
            query_id = json_dict['id']
        if 'data' in json_dict.keys():
            data = Data.from_json(json_dict['data'])
        if 'query' in json_dict.keys():
            query = json_dict['query']
        if 'duration' in json_dict.keys():
            duration = json_dict['duration']
        if 'loading' in json_dict.keys():
            loading = json_dict['loading']
        if 'queue' in json_dict.keys():
            queue = json_dict['queue']
        if 'error' in json_dict.keys():
            error = json_dict['error']
        if 'created_at' in json_dict.keys():
            created_at = json_dict['created_at']
        if 'updated_at' in json_dict.keys():
            updated_at = json_dict['updated_at']

        return QueryResponse(query_id, data, query, duration, loading, queue, error, created_at, updated_at)
