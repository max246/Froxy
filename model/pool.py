


class Pool():
    _data = {}

    def __init__(self, data):
        self._data = data

    def get_username(self):
        return self._data["username"]

    def get_password(self):
        return self._data["password"]

    def get_pool(self):
        return self._data["pool"]

    def get_algorithm(self):
        return self._data["algorithm"]

    def get_coin(self):
        return self._data["dcoin"]

    def get_scheme(self):
        return self._data["scheme"]

    def get_miner_name(self):
        return self._data["miner"]
