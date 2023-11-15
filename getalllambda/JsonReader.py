import json

from Reader import Reader

class JsonReader(Reader):
    def __init__(self, file_content):
        self.file_content = file_content

    def _parse(self):
        json_content = json.loads(self.file_content)
        return json_content

