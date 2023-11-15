import yaml
from src.Reader import Reader


class YamlReader(Reader):
    def __init__(self, file_content):
        self.file_content = file_content

    def _parse(self):
        yaml_content = yaml.safe_load(self.file_content)
        return yaml_content
