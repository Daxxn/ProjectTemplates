import os
import os.path as Path
from subprocess import Popen, run
import sys
from colorama import Fore, Back, Style

from utils.print import Printer


def currentDir(fullPath: str):
    if fullPath:
        if Path.isdir(fullPath):
            spl = Path.split(fullPath)
            if len(spl) > 1:
                return spl[1]
    return ''


# def makeDir(path: str):
#     if Path.isdir(path):
#         return True
#     subPaths = Path.split(path)
#     if Path.isdir(subPaths[0]):
#         try:
#             os.mkdir(path)
#             return True
#         except Exception as e:
#             print(f'Unable to make {path}')
#             return False
#     else:
#         if subPaths[0] == '':
#             return False
#         if makeDir(subPaths[0]):
#             os.mkdir(path)
#             return True
#         else:
#             return False

def makeDir(path: str):
    if Path.isdir(path):
        return True
    os.makedirs(path)
    return True


def copyDir(source: str, dest: str):
    if not Path.isdir(source):
        Printer.error(f'Source Dir Not Found : {source}')
        return False
    if not Path.isdir(dest):
        Printer.error(f'Destination Dir Not Found : {dest}')
        return False
    # os.system(f'rsync -a {source} {dest} --exclude /..config.json')
    process = Popen(
        # f'/usr/bin/rsync -a {source} {dest} --exclude /..config.json')
        ['/usr/bin/rsync', '-a', '-v', source,
            dest, '--exclude', '/..config.json'],
        stdout=sys.stdout,
        stderr=sys.stderr)
    process.wait()
    return True


def copyFile(source: str, dest: str):
    if not Path.isfile(source):
        Printer.error(f'Source File Not Found : {source}')
        return False
    if not Path.isdir(dest):
        Printer.error(f'Destination File Not Found : {dest}')
        return False
    process = Popen(['/usr/bin/rsync', '-a', '-v', source, dest])
    process.wait()
    return True
