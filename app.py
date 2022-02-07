# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import base64
import requests
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, world'

@app.route('/getBase64', methods=['GET'])
def getBase64():
    try:
        if request.method == 'GET':
            imageUrl = request.args.get('url')
            #imageUrl = unquote(imageUrl)
            image = base64.b64encode(requests.get(imageUrl).content).decode('utf-8')
            return jsonify({'values': image})
        else:
            return abort(400)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
