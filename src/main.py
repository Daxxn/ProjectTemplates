from utils.config import ConfigReader
from utils.licenses import LicenseManager
from utils.userInput import getUserAnswer, getUserPath, getUserSelection, getUserString
from project import Project
from utils.helpers import currentDir
from utils.print import Printer, printFileItem
from utils.templates import TemplateManager
import os.path as Path
import os
import sys
from colorama import init, Fore, Back, Style

init()


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
    print(f'{Fore.BLUE + Style.BRIGHT}Args: {Style.RESET_ALL}',
          [lang, type, sub])
    return (lang, type, sub)


def main() -> None:
    print(f'{Back.BLUE + Style.BRIGHT}\n\tTemplate Creator{Style.RESET_ALL}\n')
    lang, type, sub = parseArgs()
    templates = TemplateManager.readTemplates()
    licenses = LicenseManager.readLicenses()
    previousCWD = os.getcwd()
    print(f'{Fore.BLUE}Current Dir:{Fore.RESET} {previousCWD}')
    projectTemplate = None

    if lang and type:
        projectTemplate = TemplateManager.searchTemplates(
            templates, lang, type, sub)
    else:
        while True:
            Printer.message('\t::: Select Project Type :::', Fore.CYAN)
            lang = getUserSelection(
                'Language?', TemplateManager.getLanguages(templates))
            type = getUserSelection(
                'Project Type?', TemplateManager.getTypes(templates, lang))
            subs = TemplateManager.getSubs(templates, lang, type)
            if len(subs) > 0:
                sub = getUserSelection(
                    'Sub Type?', subs
                )
            projectTemplate = TemplateManager.searchTemplates(
                templates, lang, type, sub
            )
            if projectTemplate:
                break

    Printer.message(
        f'{Fore.GREEN + Style.BRIGHT}Project Found:\n {Style.RESET_ALL}{projectTemplate}')

    print()
    Printer.message('\t:: Project Setup ::', Fore.CYAN)

    os.chdir(previousCWD)

    # Ask for the project name:
    defaultDir = currentDir(previousCWD)
    projectName = getUserString(
        f'Whats the projects name? [{Fore.BLUE}{defaultDir}{Fore.RESET}]', defaultDir)

    # Ask what dir:
    rootPath = getUserPath(
        'The project path?', previousCWD)
    projectPath = Path.join(rootPath, projectName)

    Printer.message(projectPath, Fore.CYAN)

    projectLicense = getUserSelection('What License?', licenses)

    config = ConfigReader.readConfigFile(projectTemplate)

    newProject = Project(
        projectTemplate,
        projectName,
        projectPath,
        projectLicense,
        config
    )
    newProject.createProject()

    Printer.message('All Done!! Have fun! ;)', Fore.LIGHTBLUE_EX)


if __name__ == '__main__':
    main()
else:
    print('File is not a module.')
