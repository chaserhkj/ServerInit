#/usr/bin/env python

from bottle import route, default_app, static_file
import requests

@route('/')
def root():
    return 'Hello world!'

@route('/static/<path:path>')
def static(path):
    return static_file(path, 'static/')

@route('/<name>')
def hello(name):
    return 'Hello world to {0}!'.format(name)

@route('/google')
def google():
    res = requests.get('http://www.google.com/')
    return res.text

app = default_app()
