from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import requests

app = Flask(__name__)
api = Api(app)

api_hits = dict()

class Route_Predictions_For_Stop_ID(Resource):
    def get(self, agency_tag, stop_id):
        global api_hits
        url = "http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=" + agency_tag + "&stopId=" + stop_id

        if "predictions" in api_hits:
            api_hits["predictions"] += 1
        else:
            api_hits["predictions"] = 1

        r = requests.get(url)
        return r.content

class Route_Predictions_For_Stop_ID_For_Specific_Route(Resource):
    def get(self, agency_tag, filter_1, filter_2):
        global api_hits
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
            
        if "predictions" in api_hits:
            api_hits["predictions"] += 1
        else:
            api_hits["predictions"] = 1

        r = requests.get(url)
        return r.content

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
     app.run(debug=True,host='0.0.0.0',port=5006)
