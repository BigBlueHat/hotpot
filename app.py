import json
import urllib

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<path:doc_id>",
           methods=['HEAD', 'OPTIONS', 'GET', 'POST', 'PUT', 'DELETE'])
def from_couch(doc_id):
    params = {}
    if 'If-Match' in request.headers and request.method == 'DELETE':
        params['rev'] = request.headers.get('If-Match').strip('"')
    doc_url = 'http://localhost:5984/hotpot/' + urllib.quote_plus(doc_id)
    r = getattr(requests, request.method.lower())(doc_url,
            data=request.data, params=params)
    # TODO: make the response match couchdb's response
    return r.text

if __name__ == "__main__":
    app.run(debug=True)
