#!/usr/bin/python
# -*- coding:utf8 -*-
# 用于测试
from flask import Flask
from flask import request

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60000)
