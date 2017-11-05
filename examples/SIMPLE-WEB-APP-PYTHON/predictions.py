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

class Route_Predictions_For_Stop_ID(Resource):
    def get(self, agency_tag, stop_id):
        global api_hits
        global endpoint_access_tstamp_map
        time_diff = 31

        url = "http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=" + agency_tag + "&stopId=" + stop_id

        data_lock.acquire()

        if "predictions" in api_hits:
            api_hits["predictions"] += 1
        else:
            api_hits["predictions"] = 1

        if "predictions" in endpoint_access_tstamp_map:
            time_diff = time.time() - endpoint_access_tstamp_map["predictions"]
        else:
            endpoint_access_tstamp_map["predictions"] = time.time()

        data_lock.release()

        if time_diff > 30:
            r = requests.get(url)
            endpoint_access_tstamp_map["predictions"] = time.time()
            return r.content
        else:
            return ('Cannot access this endpoint currently. Try after 30 seconds')

class Route_Predictions_For_Stop_ID_For_Specific_Route(Resource):
    def get(self, agency_tag, filter_1, filter_2):
        global api_hits
        global endpoint_access_tstamp_map
        time_diff = 31

        url = "http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=" + agency_tag

        filter_list = []
        if "RT&" in filter_1:
            filter_list = filter_1.split("&")
            for val in filter_list:
                if "RT" in val:
                    pass
                else:
                    url = url + "&r=" + val + "&s=" + filter_2

        if "SI&" in filter_1:
            filter_list = filter_1.split("&")
            for val in filter_list:
                if "SI" in val:
                    pass
                else:
                    url = url + "&stopId=" + val + "&routeTag=" + filter_2

        data_lock.acquire()
            
        if "predictions" in api_hits:
            api_hits["predictions"] += 1
        else:
            api_hits["predictions"] = 1

        if "predictions_per_route" in endpoint_access_tstamp_map:
            time_diff = time.time() - endpoint_access_tstamp_map["predictions_per_route"]
        else:
            endpoint_access_tstamp_map["predictions_per_route"] = time.time()

        data_lock.release()

        if time_diff > 30:
            r = requests.get(url)
            endpoint_access_tstamp_map["predictions_per_route"] = time.time()
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

api.add_resource(Route_Predictions_For_Stop_ID, '/predictions/<agency_tag>/<stop_id>')
api.add_resource(Route_Predictions_For_Stop_ID_For_Specific_Route, '/predictions/<agency_tag>/<filter_1>/<filter_2>')
api.add_resource(API_Hit, '/apiHit/<api_endpoint_name>')

if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0',port=5004)
