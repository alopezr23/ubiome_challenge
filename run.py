# -*- coding: utf-8 -*-
from app import App
from flask import Flask, request
from controllers.template import TemplateController
from controllers.output import OutputController



app = App.get_instance()

@app.errorhandler(404)
def page_not_found(error):
    '''Return error 404'''
    message = '404 Not Found: The requested URL was not found on the server.'
    return OutputController().error(message)

@app.errorhandler(500)
def internal_server_error(error):
    '''Return error 500'''
    message = '500 Internal Server Error: The server encountered an internal '\
        'error or misconfiguration and was unable to complete your request.'
    return OutputController().error(message)

@app.route('/templates/<template_name>/<lang>', methods=['GET'])
def get_template(template_name, lang):
    '''Return fields from template and a language'''
    return TemplateController().get_template(template_name, lang)

if __name__ == '__main__':
    app.run()
