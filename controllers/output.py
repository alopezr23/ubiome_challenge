from flask import json

class OutputController():

    def success(self, data):
        d = {'status': True}
        for item in data: d.update(item['content']['value'])
        return json.dumps(d), {'Content-Type': 'application/json'}

    def error(self, message):
        return json.dumps({'status': False, 'error': message}), {'Content-Type': 'application/json'}
