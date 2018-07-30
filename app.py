#!/usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask
from flask import request
from utils.generateImg import *

app = Flask(__name__)

driver = openWebDriver(True)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    try:
        name = request.args['name']
    except:
        name = 'wrong parameters'
    return name


@app.route('/generateimage')
def generateimage():
    generateImg(driver=driver)
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60000)
