from utils.fileTree import printTree
from utils.templates import TemplateManager
import sys


def parseArgs():
    lang = ''
    type = ''
    sub = ''
    if len(sys.argv) == 4:
        lang = sys.argv[1]
        type = sys.argv[2]
        sub = sys.argv[3]
    elif len(sys.argv) == 3:
        lang = sys.argv[1]
        type = sys.argv[2]
    print([lang, type, sub])
    return (lang, type, sub)


def main() -> None:
    lang, type, sub = parseArgs()
    templates = TemplateManager.readTemplates()
    printTree(templates)


if __name__ == '__main__':
    main()
else:
    print('File is not a module.')
