from models.template import Template
from flask import Flask, Response
from output import OutputController

class TemplateController(OutputController):

    def get_template(self, name, lang):
        template = Template()
        data = template.get(name, lang)
        if not data: return self.error('Template Not Found') #return error if data is empty
        return self.success(data)
