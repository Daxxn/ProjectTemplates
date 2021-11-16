from json import load
from utils.templates import Template
import os.path as Path


class Config:
    def __init__(self) -> None:
        self.scripts: list[str] = []


class ConfigReader:
    def __init__(self, template: Template) -> None:
        self.template = template

    def readConfigFile(self):
        try:
            with open(Path.join(self.template.FullPath, '..config.json'), 'r') as file:
                data = load(file)
        except Exception as e:
            print(str(e))
