# -*- coding: utf-8 -*-
import os
import datetime
from flask import Flask
from mongokit import *


connection = Connection(os.environ.get('MONGODB_URL'))
db = connection[os.environ.get('MONGODB_DATABASE')]

@connection.register
class Template(Document):
    __database__ = os.environ.get('MONGODB_DATABASE')
    __collection__ = 'templates'

    structure = {
        'name': str,
        'content': dict,
        "created_at": datetime.datetime,
    }
    default_values = {'created_at':datetime.datetime.now()}
    i18n = ['content']
    use_dot_notation = True

    def search_template_lang(self, template, lang):
        '''Search fields from template and a language'''
        return db.templates.aggregate([
            {'$match': {'name': template}},
            {'$unwind': '$content'},
            {'$match': {'content.lang': lang}},
            {'$project': { 'name' : 1, 'content.value': 1 }}
        ])

    def get(self, template, lang):
        '''Response fields from template and a language'''
        result = self.search_template_lang(template, lang)
        if not result['result'] and lang != os.environ.get('DEFAULT_LANG'):
            return self.get(template, os.environ.get('DEFAULT_LANG'))
        return result['result']
