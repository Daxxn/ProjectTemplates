import os.path as Path
from colorama import Fore, Back, Style

from utils.print import Printer


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
    # print(msg)
    # for s in range(len(selections)):
    #     print(f'{s} ) {selections[s]}')
    if useIndex:
        Printer.numberedList(msg, selections)
    while True:
        inputStr = input(f'{Fore.GREEN}>{Fore.RESET}  ')
        try:
            index = int(inputStr)
            if index >= 0 and index < len(selections):
                return selections[index]
        except ValueError:
            for sel in selections:
                if str(sel) == inputStr or (ignoreCase and str(sel).lower() == inputStr.lower()):
                    return sel
        print(f'{Fore.RED}No match. Try Again{Fore.RESET}')


def getUserString(msg: str, defaultResponse: str = None):
    if defaultResponse:
        inp = ''
        if len(msg) > 80:
            inp = input(f'{msg}\n{Fore.GREEN}>  {Fore.RESET}')
        else:
            inp = input(f'{msg}{Fore.GREEN}>  {Fore.RESET}')
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
    print(f'{msg} {Fore.YELLOW + Style.DIM}: Append path \'./\'{Style.RESET_ALL}')
    print(Fore.CYAN + f'   {defaultPath}' + Style.RESET_ALL)
    while True:
        inp = input()
        if inp:
            if not inp.startswith('./') or inp.startswith('/home'):
                return Path.normpath(inp)
            else:
                inp = inp.strip('./')
                combPath = Path.join(defaultPath, inp)
                return Path.normpath(combPath)
        else:
            return defaultPath
