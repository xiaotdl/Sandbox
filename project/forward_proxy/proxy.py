# -*- coding: utf-8 -*-

"""
Usage Examples:
http://localhost:5000/
http://localhost:5000/proxy/http://www.google.com
http://localhost:5000/files/123.html
"""

import requests

from flask import Flask, Response, stream_with_context
from flask import request, send_from_directory


app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/proxy/<path:url>')
def proxy(url):
    req = requests.get(url, stream = True)
    return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])

@app.route('/files/<path:path>')
def files(path):
    return send_from_directory('files', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
