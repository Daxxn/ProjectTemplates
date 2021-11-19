from colorama import Fore, Back, Style

# region Path Tree Printer (WIP)
# None of this is working right at the moment. it works with the
# old fileInfo tree class. Need to implement a version for the
# template class.

tableCodes = {
    'top': '\u250F',
    'vert': '\u2503',
    'rightAngle': '\u2517'
}


def printTree(file) -> None:
    print('Printing Tree:')
    print(f'{tableCodes["top"]} {file.name}')
    depth = 1
    for i in range(len(file.children)):
        depth = printFileItem(file.children[i], depth, i, len(file.children))
    print(tableCodes['rightAngle'])


def printFileItem(file, depth: int, index: int, length: int) -> str:
    treeLegs = ''
    spacing = ''
    for d in range(depth):
        if d > 0 and d == (depth - 1):
            if index == (length - 1):
                treeLegs += tableCodes['rightAngle']
            elif index == 0:
                treeLegs += tableCodes['top']
            else:
                treeLegs += tableCodes['vert']
        else:
            treeLegs += tableCodes['vert']
        spacing += ' '

    print(f'{treeLegs}{spacing}{file.Name}')
    if len(file.children) > 0:
        depth += 1
        for i in range(len(file.children)):
            printFileItem(file.children[i], depth, i, len(file.children))
        depth -= 1
    return depth
# endregion


class Printer:
    @staticmethod
    def message(message: str, foreground: Fore = None, reset: bool = True):
        if foreground:
            print(
                f'{foreground if foreground else ""}{message} {Fore.RESET if reset else ""}')
        else:
            print(message)

    @staticmethod
    def messageBack(message: str, fore: Fore, back: Back, reset: bool = True):
        print(
            f'{fore + back}{message} {Style.RESET_ALL if reset else ""}')

    @staticmethod
    def error(message: str, reset: bool = True):
        Printer.message(message, Fore.RED, reset)

    @staticmethod
    def success(message: str = None, reset: bool = True):
        if message:
            Printer.message(f'  {message}', Fore.GREEN, reset)
        else:
            Printer.message('  Success', Fore.GREEN, reset)

    @staticmethod
    def status(message: str, reset: bool = True):
        print(
            f' {Fore.CYAN + Style.BRIGHT}{message}...{Style.RESET_ALL if reset else ""}')

    @staticmethod
    def numberedList(title: str, list: list):
        print(f'{Fore.BLUE}{title}{Fore.RESET}')
        length = len(list)
        if length > 0:
            for l in range(length):
                print(f'{Style.BRIGHT}{l}){Style.RESET_ALL} {list[l]}')
        else:
            print(f'{Fore.RED + Style.DIM}\tNo items in list{Style.RESET_ALL}')

    @staticmethod
    def list(title: str, list: list):
        print(f'{Fore.BLUE}{title}{Fore.RESET}')
        length = len(list)
        if length > 0:
            for l in range(length):
                print(f'{Style.BRIGHT}\t){Style.RESET_ALL} {list[l]}')
        else:
            print(f'{Fore.RED + Style.DIM}\tNo items in list{Style.RESET_ALL}')
