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

@app.route('/wx', methods=['GET', 'POST'])
def wx():
    if request.method == 'POST':
        try:
            webData = request.form
            print 'Handle Post webdata is ', webData
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = 'test'
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg
            else:
                print '暂不处理'
                return 'success'
        except Exception, Argment:
            return Argment
    else:
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
