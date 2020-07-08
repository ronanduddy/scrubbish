import json
import time


class JsonHelper:
    def __init__(self, filename):
        self.filename = filename
        self.directory = "json"
        self.creation = time.time()

    def dump(self, data):
        with open(self._new_file(), "w+") as file:
            json.dump(data, file)

    def read(self):
        data = None

        with open(self.filename, "r") as file:
            data = json.load(file)

        return data

    def _new_file(self):
        return f"{self.directory}/{self.filename}_{self.creation}.json"
