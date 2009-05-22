#!/usr/bin/env python

from distutils.core import setup

setup(name='django-heroism',
      version='0.1',
      description='Middleware for SSL detection in Django, when the site runs behind Nginx as a proxy',
      author='Ross Dakin',
      author_email='rossdakin@gmail.com',
      url='http://github.com/rossdakin/django-heroism/tree/master',
      packages=['heroism'],
)
