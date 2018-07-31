#!/usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask
from flask import request
from biz.generateImg import *
import datetime
import time
import sys
import logging

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

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


@app.route('/generateimage', methods=['GET', 'POST'])
def generateimage():
    t1 = time.mktime(datetime.datetime.now().timetuple())
    generateImg(driver=driver)
    t2 = time.mktime(datetime.datetime.now().timetuple())
    logging.info('generateimage time use:%dms' % (t2 - t1))
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60000)
