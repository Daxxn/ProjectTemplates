import os
import os.path as Path


class Template:
    def __init__(self, lang: str, type: str, sub: str = '') -> None:
        self.lang = lang
        self.type = type
        self.sub = sub

    def __str__(self):
        return f'{self.Lang} : {self.Type} : {self.Sub}\n  Path : ./templates/{self.lang}/{self.type}/{self.sub}'

    def equals(self, lang: str, type: str, sub: str = ''):
        if self.lang == lang and self.type == type:
            if self.sub and sub:
                if self.sub == sub:
                    return True
            else:
                return True
        return False

    def __eq__(self, o: object) -> bool:
        if isinstance(self, o):
            if self.lang == o.lang and self.type == o.type and self.sub == o.sub:
                return True
        return False

    @property
    def Lang(self):
        if self.lang:
            return self.lang.strip('_')

    @property
    def Type(self):
        if self.type:
            return self.type.strip('_')

    @property
    def Sub(self):
        if self.sub:
            return self.sub.strip('_')

    @property
    def FullPath(self):
        return Path.join(TemplateManager.getRootTemplatePath(), self.lang, self.type, self.sub)


class TemplateManager:
    def __init__(self) -> None:
        self.languages: list[str] = []
        self.types: list[str] = []
        self.sub: list[str] = []

    @staticmethod
    def getValues(templates: list[Template], lang: str = '', type: str = '', sub: str = ''):
        output: list[str] = []
        if len(templates) > 0:
            if lang:
                for temp in templates:
                    if not output.__contains__(temp.lang) and temp.lang == lang:
                        if type:
                            if type == temp.type and not output.__contains__(temp.type):
                                if sub:
                                    if sub == temp.sub and not output.__contains__(temp.sub):
                                        output.append(temp)
                                else:
                                    output.append(temp)
                            else:
                                output.append(temp)
                        else:
                            output.append(temp)
            else:
                for temp in templates:
                    if not output.__contains__(temp.lang):
                        output.append(temp)

    @staticmethod
    def getLanguages(templates: list[Template]):
        output: list[str] = []
        if len(templates) > 0:
            for temp in templates:
                if not output.__contains__(temp.lang):
                    output.append(temp.lang)
        return output

    @staticmethod
    def getTypes(templates: list[Template], lang: str):
        output: list[str] = []
        if len(templates) > 0:
            for temp in templates:
                if temp.lang == lang and not output.__contains__(temp.type):
                    output.append(temp.type)
        return output

    @staticmethod
    def getSubs(templates: list[Template], lang: str, type: str):
        output: list[str] = []
        if len(templates) > 0:
            for temp in templates:
                if temp.lang == lang and temp.type == type and temp.sub and not output.__contains__(temp.sub):
                    output.append(temp.sub)
        return output

    @staticmethod
    def getRootTemplatePath():
        return '/home/Daxxn/Code/Python/Projects/TemplateCreator/src/templates/'

    @staticmethod
    def readTemplates():
        try:
            templates: list[Template] = []
            templatePath = TemplateManager.getRootTemplatePath()
            languages = os.listdir(templatePath)
            for lang in languages:
                if lang.startswith('_'):
                    for type in os.listdir(Path.join(templatePath, lang)):
                        if type.startswith('_'):
                            subs = os.listdir(
                                Path.join(templatePath, lang, type))
                            if len(subs) > 0:
                                isSubs = False
                                for sub in subs:
                                    if sub.startswith('_'):
                                        templates.append(
                                            Template(lang, type, sub))
                                        isSubs = True
                                if not isSubs:
                                    templates.append(Template(lang, type))
                            else:
                                templates.append(Template(lang, type))
            return templates
        except Exception as e:
            print(str(e))

    @staticmethod
    def searchTemplates(templates: list[Template], lang: str, type: str, sub: str = ''):
        for t in templates:
            if t.equals(lang, type, sub):
                return t
