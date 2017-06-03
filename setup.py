# -*- coding: utf-8 -*-
import os
from mongokit import *
from models.template import Template

connection = Connection(os.environ.get('MONGODB_URL'))
db = connection[os.environ.get('MONGODB_DATABASE')]

def seed():
    '''Add seed data to the database'''
    connection.register([Template])
    template_header = connection.Template()

    template_header.name = 'header'
    template_header.content = {
        'acction_1': 'Microbiome Testing',
        'acction_2': 'For Doctors',
        'acction_3': 'About Us',
        'acction_4': 'Meet the Microbiome',
        'acction_5': 'Explorer',
        'acction_6': 'Sign In'
    }
    template_header.save()

    template_header.set_lang('es')
    template_header.content = {
        'acction_1': 'Prueba de microbioma',
        'acction_2': 'Para doctores',
        'acction_3': 'Nosotros',
        'acction_4': 'Conoce el microbioma',
        'acction_5': 'Explora',
        'acction_6': 'Iniciar sessión'
    }
    template_header.save()

    template_body = connection.Template()

    template_body.name = 'body'
    template_body.content = {
        'title_1': 'Actionable Insights to Improve Your Gut Health',
        'content_1': 'uBiome\'s SmartGut™ is the world\'s first sequencing-based '\
            'clinical microbiome screening test, providing detailed and accurate '\
            'information to help you understand your gut health.'
    }
    template_body.save()

    template_body.set_lang('es')
    template_body.content = {
        'acction_1': 'Información útil para mejorar tu salud intestinal',
        'acction_2': 'Ubiome SmartGut™ es la primera prueba del mundo para la '\
        'detección de microbiomas basada en secuencias, está provee información '\
        'detallada y precisa que permite entender la salud intestinal.'
    }
    template_body.save()

    template_footer = connection.Template()
    template_footer.name = 'footer'
    template_footer.content = {
        'acction_1': 'Careers',
        'acction_2': 'Read the uBiome Blog'
    }
    template_footer.save()

    template_footer.set_lang('es')
    template_footer.content = {
        'acction_1': 'Empleos',
        'acction_2': 'Lee el Blog de uBiome'
    }
    template_footer.save()


if __name__ == '__main__':
    seed()
