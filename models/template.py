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
        '_id': str,
        'name': str,
        'content': dict,
        "created_at": datetime.datetime,
    }
    default_values = {'created_at':datetime.datetime.now()}
    i18n = ['content']
    use_dot_notation = True

    def search_template_lang(self, template, lang):
        return db.templates.aggregate([
            {'$match': {'name': template}},
            {'$unwind': '$content'},
            {'$match': {'content.lang': lang}},
            {'$project': { 'name' : 1, 'content.value': 1 }}
        ])
        # if not result['result']:
        #     return self.search_template_lang(template, os.environ.get('DEFAULT_LANG'))
        # return result

    def get(self, template, lang):
        result = self.search_template_lang(template, lang)
        if not result['result'] and lang != os.environ.get('DEFAULT_LANG'):
            return self.get(template, os.environ.get('DEFAULT_LANG'))
        return result['result']


# connection.register([Template])
# strings = connection.Template()
# strings['_id'] = 'bp1'
# strings.name = "texto1"
# strings.content = {"body": "How are you ?"}
# strings.set_lang('fr')
# strings.content = {"body": "Comment allez-vous ?"}
# strings.save()

# raw_strings = db.i18n.find_one({'template':'texto1'})
# print raw_strings
