import json


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename) as f:
                return json.load(f)
        except Exception as e:
            print(e)
            raise e
