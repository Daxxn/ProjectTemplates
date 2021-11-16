import os
import os.path as Path


def currentDir(fullPath: str):
    if fullPath:
        if Path.isdir(fullPath):
            spl = Path.split(fullPath)
            if len(spl) > 1:
                return spl[1]
    return ''


def makeDir(path: str):
    if Path.isdir(path):
        return True
    subPaths = Path.split(path)
    if Path.isdir(subPaths[0]):
        try:
            os.mkdir(path)
            return True
        except Exception as e:
            print(f'Unable to make {path}')
            return False
    else:
        if subPaths[0] == '':
            return False
        if makeDir(subPaths[0]):
            os.mkdir(path)
            return True
        else:
            return False


def copyDir(source: str, dest: str):
    if not Path.isdir(source):
        print('Source is bad')
        return False
    if not Path.isdir(dest):
        print('Destination is bad')
        return False
    os.system(f'rsync -a {source} {dest} --exclude /..config.json')
