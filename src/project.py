from colorama.ansi import Back, Fore
from utils.helpers import copyDir, copyFile, makeDir
from utils.templates import Template
from utils.licenses import License
from utils.config import Config
from utils.print import Printer
from subprocess import Popen
import shlex
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
        Printer.status('creating project')
        Printer.status('making folder')
        # Make the project folder,
        if makeDir(self.path):
            Printer.status('copying template')
            # Copy the project files from the template
            try:
                tempSuccess = copyDir(self.template.FullPath, self.path)
            except Exception as e:
                Printer.error(f'Unable to copy template.\n{e}')

            if tempSuccess:
                Printer.status('switching to folder')
                os.chdir(self.path)
                Printer.status('making license')
                try:
                    copyFile(self.license.path, self.path)
                    Printer.success('license created')
                except Exception as e:
                    Printer.error(f'Unable to create license.\n{e}')

                Printer.status('initializing project')
                try:
                    Printer.status('running config scripts')
                    self.runConfig()
                    Printer.success('config scripts complete.')
                except Exception as e:
                    Printer.error(f'Unable to init project.\n{e}')

                try:
                    Printer.status('running dependency check')
                    self.runDependencyCheck()
                except Exception as e:
                    Printer.error(f'Unable to check dependencies.\n{e}')

                Printer.success('initialization complete.')
        else:
            Printer.error(
                'Unable to create project. Failed to create project folder.')

    def runConfig(self):
        if self.config.pm and self.config.install:
            if isinstance(self.config.install, list):
                for s in self.config.install:
                    cmd = shlex.split(f'{self.config.pm} {s}')
                    process = Popen(
                        cmd,
                        stdout=sys.stdout,
                        stderr=sys.stderr)
                    process.wait()
            elif isinstance(self.config.install, str):
                cmd = shlex.split(
                    f'{self.config.pm} {self.config.install}'
                )
                process = Popen(
                    cmd,
                    stdout=sys.stdout,
                    stderr=sys.stderr
                )
                process.wait()
            else:
                Printer.error(
                    'Unable to auto-init project. Unknown install command type')
        else:
            Printer.error(
                'Unable to auto-init project. missing commands from \'..config.json\' file.')

    def runDependencyCheck(self):
        if self.config.pm and self.config.depCheck:
            if self.config.dependencies and len(self.config.dependencies) > 0:
                Printer.message('For now, just printing the dependencies...')
                Printer.list('Dependencies', self.config.dependencies)
            else:
                Printer.error('No dependencies found.')

            # For now Im just going to print the installed dependencies.
            process = Popen(
                [self.config.pm, self.config.depCheck],
                stdout=sys.stdout, stderr=sys.stderr
            )
            process.wait()
        else:
            Printer.error(
                'Unable to run dep check. missing commands in \'..config.json\' file.'
            )

    def runConfigDep(self, dependency: str):
        Printer.messageBack(
            'Run Dependency Check... (WIP)', Fore.BLACK, Back.YELLOW
        )
