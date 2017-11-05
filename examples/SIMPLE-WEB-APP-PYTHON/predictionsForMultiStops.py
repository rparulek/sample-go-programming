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

class Route_Predictions_For_Multiple_Stops(Resource):
    def get(self, agency_tag, stops):
        global api_hits
        global endpoint_access_tstamp_map
        time_diff = 31

        url = "http://webservices.nextbus.com/service/publicXMLFeed?command=predictionsForMultiStops&a=" + agency_tag

        stops_list = stops.split("&")
        for stop in stops_list:
            url = url + "&stops=" + stop

        data_lock.acquire()

        if "predictionsForMultiStops" in api_hits:
            api_hits["predictionsForMultiStops"] += 1
        else:
            api_hits["predictionsForMultiStops"] = 1

        if "predictionsForMultiStops" in endpoint_access_tstamp_map:
            time_diff = time.time() - endpoint_access_tstamp_map["predictionsForMultiStops"]
        else:
            endpoint_access_tstamp_map["predictionsForMultiStops"] = time.time()

        data_lock.release()

        if time_diff > 30:
            r = requests.get(url)
            endpoint_access_tstamp_map["predictionsForMultiStops"] = time.time()
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

api.add_resource(Route_Predictions_For_Multiple_Stops, '/predictionsForMultiStops/<agency_tag>/<stops>')
api.add_resource(API_Hit, '/apiHit/<api_endpoint_name>')

if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0',port=5005)
