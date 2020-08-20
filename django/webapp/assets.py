from dictor import dictor
from webapp.config import ASSETS_CONFIG


class Assets:
    JS_ID = "js_list"
    CSS_ID = "css_list"

    def __init__(self, name):
        """constructor"""
        self.name = name
        self.config = ASSETS_CONFIG
        self.js_list = self.buildJsList()
        self.css_list = self.buildCssList()

    def __str__(self):
        """ str view """
        return self.name

    def getJavascriptDependencies(self):
        """getter - list of js dependencies"""
        return self.js_list

    def getCssDependencies(self):
        """getter - list of css dependencies"""
        return self.css_list

    def buildJsList(self):
        """build js list using context and config"""
        return dictor(self.config, ".".join([self.name, self.JS_ID]))

    def buildCssList(self):
        """build css list using context and config"""
        return dictor(self.config, ".".join([self.name, self.CSS_ID]))
