import os.path as Path
from colorama import Fore, Back, Style


def getUserAnswer(msg: str, defaultYes: bool = True):
    yesNoDisp = '[Y/n]' if defaultYes else '[y/N]'
    while True:
        inputStr = input(f'{msg} : {yesNoDisp}  ')
        if len(inputStr) == 1:
            if inputStr.lower() == 'y':
                return True
            elif inputStr.lower() == 'n':
                return False
        elif not inputStr:
            return defaultYes


def getUserSelection(msg: str, selections: list, useIndex: bool = True, ignoreCase: bool = True):
    print(msg)
    for s in range(len(selections)):
        print(f'{s} ) {selections[s]}')
    while True:
        inputStr = input('>  ')
        try:
            index = int(inputStr)
            if index >= 0 and index < len(selections):
                return selections[index]
        except ValueError:
            for sel in selections:
                if str(sel) == inputStr or (ignoreCase and str(sel).lower() == inputStr.lower()):
                    return sel
        print('No match.')


def getUserString(msg: str, defaultResponse: str = None):
    if defaultResponse:
        inp = input(f'{msg}  ')
        if inp:
            return inp
        else:
            return defaultResponse
    else:
        while True:
            inp = input(msg)
            if inp:
                return inp


def getUserPath(msg: str, defaultPath: str):
    print(f'{msg}')
    print(Fore.CYAN + f'  {defaultPath}' + Style.RESET_ALL)
    while True:
        inp = input()
        if inp:
            if inp.startswith('^'):
                inp = inp.strip('^')
                return Path.normpath(inp)
            else:
                combPath = Path.join(defaultPath, inp)
                return Path.normpath(combPath)
        else:
            return defaultPath
