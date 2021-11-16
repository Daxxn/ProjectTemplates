from project import Project
from utils.helpers import currentDir
from utils.templates import TemplateManager
import os.path as Path
import os
import sys

from utils.userInput import getUserAnswer, getUserPath, getUserSelection, getUserString


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
    print('Args: ', [lang, type, sub])
    return (lang, type, sub)


def main() -> None:
    lang, type, sub = parseArgs()
    templates = TemplateManager.readTemplates()
    previousCWD = os.getcwd()
    print(previousCWD)
    projectTemplate = None

    if lang and type:
        projectTemplate = TemplateManager.searchTemplates(
            templates, lang, type, sub)
    else:
        while True:
            print('::: Select Project Type :::')
            print()

            lang = getUserSelection(
                'Select Language:', TemplateManager.getLanguages(templates))
            type = getUserSelection(
                'Select Type:', TemplateManager.getTypes(templates, lang))
            subs = TemplateManager.getSubs(templates, lang, type)
            if len(subs) > 0:
                sub = getUserSelection(
                    'Select Sub:', subs)
            projectTemplate = TemplateManager.searchTemplates(
                templates, lang, type, sub)
            if projectTemplate:
                break

    print(projectTemplate.toString())

    print()
    print(':: Project Setup ::')

    os.chdir(previousCWD)

    # Ask for the project name:
    defaultDir = currentDir(previousCWD)
    projectName = getUserString(
        f'Whats the projects name? [{defaultDir}]', defaultDir)

    # Ask what dir:
    projectPath = getUserPath(
        'The project path?', Path.join(defaultDir, projectName))

    newProject = Project(projectTemplate, projectName, projectPath)
    newProject.createProject()


if __name__ == '__main__':
    main()
else:
    print('File is not a module.')
