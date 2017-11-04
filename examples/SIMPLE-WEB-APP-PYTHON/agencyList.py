from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import requests

app = Flask(__name__)
api = Api(app)

api_hits = dict()

class Agency_List(Resource):
    def get(self):
        global api_hits
        url = "http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList"

        if "agencyList" in api_hits:
            api_hits["agencyList"] += 1
        else:
            api_hits["agencyList"] = 1

        r = requests.get(url)
        return r.content

class API_Hit(Resource):
    def get(self, api_endpoint_name):
        if api_endpoint_name in api_hits:
            pass
        else:
            api_hits[api_endpoint_name] = 0

        return ('Endpoint access count: ' + str(api_hits[api_endpoint_name]))

api.add_resource(Agency_List, '/agencyList')
api.add_resource(API_Hit, '/apiHit/<api_endpoint_name>')

if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0',port=5001)
