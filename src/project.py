from utils.helpers import copyDir, makeDir
from utils.templates import Template


class Project:
    def __init__(self, template: Template, name: str, path: str) -> None:
        self.template = template
        self.name = name
        self.path = path

    def __str__(self) -> str:
        return f'{self.name} | {self.template}'

    def createProject(self):
        # Make the project folder,
        if makeDir(self.path):
            # Copy the project files from the template
            copyDir(self.template.FullPath, self.path)
            # Init any files? Still not sure how thats gonna work.
            # Run any installs or scripts
