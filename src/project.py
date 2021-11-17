from utils.helpers import copyDir, makeDir
from utils.templates import Template
from utils.licenses import License
from utils.config import Config
from subprocess import Popen
import os
import sys


class Project:
    def __init__(self, template: Template, name: str, path: str, license: License, config: Config) -> None:
        self.template = template
        self.name = name
        self.path = path
        self.license = license
        self.config = config

    def __str__(self) -> str:
        return f'{self.name} | {self.template}'

    def createProject(self):
        # Make the project folder,
        if makeDir(self.path):
            # Copy the project files from the template
            tempSuccess = copyDir(self.template.FullPath, self.path)

            # Copy License into project
            licSuccess = copyDir(self.license.path, self.path)

            # Init any files and Run any installs or scripts
            initSuccess = self.runConfig()

    def runConfig(self):
        try:
            if self.config.scripts:
                if isinstance(self.config.scripts, list):
                    for s in self.config.scripts:
                        # result = os.system(s)
                        process = Popen(s, shell=True)
                        # process = Popen(s, shell=True, stdout=sys.stdout)
                        process.wait()
                elif isinstance(self.config.scripts, str):
                    process = Popen(self.config.scripts, shell=True)
                    process.wait()
            if self.config.dependencies and self.config.pm:
                if len(self.config.dependencies) > 0:
                    for dep in self.config.dependencies:
                        self.runConfigDep(dep)
        except Exception as e:
            print(str(e))

    def runConfigDep(self, dependency: str):
        try:
            process = Popen(f'{self.config.pm} version {dependency}')
            status = process.wait()
            if status:
                with process.stdout as file:
                    lines = file.readlines()
                    for l in lines:
                        print(l)
        except Exception as e:
            print(str(e))
