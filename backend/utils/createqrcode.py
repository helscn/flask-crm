#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from flask import Response, request
from io import BytesIO
import qrcode


def request_parse(req_data):
    '''解析请求数据并以json形式返回'''
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data


def CreateQRCode():
    data = request_parse(request).get('data')
    print('Data:', data)
    qr = qrcode.make(data=data)
    img = BytesIO()
    qr.save(img, format='JPEG')
    img_bytes = img.getvalue()
    resp = Response(img_bytes, mimetype="image/jpeg")
    return resp
