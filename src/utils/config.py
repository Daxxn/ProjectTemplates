from json import load
from utils.templates import Template
import os.path as Path


class Config:
    def __init__(self) -> None:
        self.pm: str = ''
        self.dependencies: list[str] = []
        self.scripts: list[str] = []

    @staticmethod
    def deserialize(data: dict):
        self = Config()
        if data['scripts']:
            self.scripts = data['scripts']
        if data.dependencies:
            self.dependencies = data['dependencies']
        if data['pm']:
            self.pm = data['pm']
        return self


class ConfigReader:
    @staticmethod
    def readConfigFile(template: Template):
        try:
            with open(Path.join(template.FullPath, '..config.json'), 'r') as file:
                return Config.deserialize(load(file))
        except Exception as e:
            print(str(e))
