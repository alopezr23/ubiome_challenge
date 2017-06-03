# -*- coding: utf-8 -*-
from flask import json

class OutputController():

    def success(self, data):
        '''Data output format'''
        d = {'status': True, 'fields': {}}
        for item in data: d['fields'].update(item['content']['value'])
        return json.dumps(d), {'Content-Type': 'application/json'}

    def error(self, message):
        '''Error output format'''
        return json.dumps({'status': False, 'error': message}), {'Content-Type': 'application/json'}
