#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
# Author: linyl
# Created Time : 五 12/21 15:58:09 2018
# File Name: main.py
# Description:
"""

import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/wx')
def wx():
    try:
        data = request.args
        if len(data) == 0:
            return 'hello, this is handle view'
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')
        echostr = data.get('echostr')
        token = 'I7aPyH4HMzajIUKy4rY1OJGB4xesIJ5o'
        
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print "API:/wx GET func: hashcode: %s, signature: %s" % (hashcode, signature) 
        if hashcode == signature:
            return echostr
        else:
            return ""
    except Exception, Argument:
        return Argument

if __name__ == '__main__':
    app.run('0.0.0.0', port=2333, debug=True)
