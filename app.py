# -*- coding: utf-8 -*-
from flask import Flask


class App():

    instance = None

    @staticmethod
    def get_instance():
        if App.instance is None:
            App.instance = Flask(__name__)
            App.instance.config.from_object('config')

        return App.instance
