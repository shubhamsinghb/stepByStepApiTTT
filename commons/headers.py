class Headers:
    def __init__(self):
        self.headers = {}

    def add_header_value(self, key, value):
        self.headers[key] = value

    def set_json_header(self):
        self.headers["Content-Type"] = "application/json"
        return self.headers

    def get_header(self):
        return self.headers
