from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import requests
import time
import threading

app = Flask(__name__)
api = Api(app)

api_hits = dict()
endpoint_access_tstamp_map = dict()
data_lock = threading.Lock()

class Schedule(Resource):
    def get(self, agency_tag, route_tag):
        global api_hits
        global endpoint_access_tstamp_map
        time_diff = 31

        url = "http://webservices.nextbus.com/service/publicXMLFeed?command=schedule&a=" + agency_tag + "&r=" + route_tag

        data_lock.acquire()

        if "schedule" in api_hits:
            api_hits["schedule"] += 1
        else:
            api_hits["schedule"] = 1

        if "schedule" in endpoint_access_tstamp_map:
            time_diff = time.time() - endpoint_access_tstamp_map["schedule"]
        else:
            endpoint_access_tstamp_map["schedule"] = time.time()

        data_lock.release()

        if time_diff > 30:
            r = requests.get(url)
            endpoint_access_tstamp_map["schedule"] = time.time()
            return r.content
        else:
            return ('Cannot access this endpoint currently. Try after 30 seconds')

class API_Hit(Resource):
    def get(self, api_endpoint_name):
        if api_endpoint_name in api_hits:
            pass
        else:
            api_hits[api_endpoint_name] = 0

        return ('Endpoint access count: ' + str(api_hits[api_endpoint_name]))

api.add_resource(Schedule, '/schedule/<agency_tag>/<route_tag>')
api.add_resource(API_Hit, '/apiHit/<api_endpoint_name>')

if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0',port=5006)
