import os.path as Path
import os


class License:
    def __init__(self, name: str, path: str) -> None:
        self.name = name
        self.path = path

    def __str__(self) -> str:
        return self.name


class LicenseManager:
    @staticmethod
    def getLicensesPath():
        return '/home/Daxxn/Code/Python/Projects/TemplateCreator/src/licenses'

    @staticmethod
    def readLicenses():
        try:
            output: list[License] = []
            licensesPath = LicenseManager.getLicensesPath()
            files = os.listdir(licensesPath)
            for f in files:
                output.append(License(f, Path.join(licensesPath, f)))
            return output
        except Exception as e:
            print(str(e))

    def searchLicenses(licenses: list[License], name: str):
        for l in licenses:
            if l.name == name:
                return l
