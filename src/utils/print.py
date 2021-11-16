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
