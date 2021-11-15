import os
import os.path as Path

from utils.fileTree import FileInfo


class Template:
    def __init__(self) -> None:
        self.path = ''


class TemplateManager:
    def __init__(self) -> None:
        pass

    @staticmethod
    def readTemplates():
        try:
            templates = FileInfo(Path.join(os.getcwd(), 'src', 'templates'))
            for t in templates.children:
                print(t.Name)

        except Exception as e:
            print(str(e))
