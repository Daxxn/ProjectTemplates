import os.path as Path
import os
from uuid import uuid4 as uid, UUID


class FileInfo:
    def __init__(self, path: str = None, parentId: UUID = None) -> None:
        exists = Path.exists(path)
        if exists:
            isTemp = Path.basename(path).startswith('_')
            if isTemp:
                self.id = uid()
                self.parentId = parentId
                self.isFile = Path.isfile(path)
                self.name: str = Path.basename(path)
                self.fullPath: str = path
                self.children: list[FileInfo] = []
                self.ext: str = ''
                self.isImage: bool = self.checkExt(path)
                if not self.isFile:
                    self.populateChildren(path)
                else:
                    self.ext: str = Path.splitext(path)[1]

    def populateChildren(self, rootDir: str):
        if Path.isdir(rootDir):
            paths = os.listdir(rootDir)
            for path in paths:
                temp = FileInfo(Path.join(rootDir, path), self.id)
                self.children.append(temp)
        else:
            return

    @staticmethod
    def checkExt(file: str):
        if Path.isdir(file):
            if file.startswith('_'):
                return True
        return False

    def getChildrenIds(self):
        output = []
        for ch in self.children:
            output.append(ch.id)
        return output

    def searchTree(self, id: UUID):
        if str(self.id) == id:
            return self
        if len(self.children) > 0:
            for child in self.children:
                result = child.searchTree(id)
                if result != None:
                    return result
        else:
            return None

    def getChild(self, id: UUID):
        output = None
        for ch in self.children:
            if id == ch.id:
                output = ch
                break
        return output

    @property
    def Name(self):
        return self.name

    @property
    def FullPath(self):
        return self.fullPath

    @property
    def AllowedExt():
        return [
            '.png',
            '.jpg',
            '.bmp',
            '.jpeg',
            '.PNG'
        ]


tableCodes = {
    'horz': '\u2500',
    'vert': '\u2503',
    'rightAngle': '\u2514'
}


def printTree(file: FileInfo) -> None:
    print(tableCodes['horz'])
    print(tableCodes['rightAngle'])
    print(tableCodes['vert'])
