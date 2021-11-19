from json import load
from utils.templates import Template
import os.path as Path


class Config:
    def __init__(self) -> None:
        self.pm: str = ''
        self.install: str = ''
        self.depCheck: str = ''
        self.dependencies: list[str] = []

    @staticmethod
    def deserialize(data: dict):
        self = Config()
        if data['pm']:
            self.pm = data['pm']
        if data['install']:
            self.install = data['install']
        if data['depCheck']:
            self.depCheck = data['depCheck']
        if data['dependencies']:
            self.dependencies = data['dependencies']
        return self


class ConfigReader:
    @staticmethod
    def readConfigFile(template: Template):
        try:
            path = Path.join(template.FullPath, '..config.json')
            if (Path.isfile(path)):
                with open(path, 'r') as file:
                    return Config.deserialize(load(file))
            return None
        except Exception as e:
            print(str(e))
