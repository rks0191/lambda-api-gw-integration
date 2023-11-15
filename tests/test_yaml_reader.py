from unittest import TestCase

from package.YamlReader import YamlReader


def readFile(filePath):
    content = ""
    with open(filePath, "r") as file:
        content = file.read()
        file.close()
        return content


class TestYamlReader(TestCase):
    def test_yaml_reader(self):
        yaml_file_content = readFile("../prices/advertiser_100.yaml")
        reader = YamlReader(yaml_file_content)
        parsed = reader.parse()
        print(parsed.to_dict())
