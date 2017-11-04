from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import requests

app = Flask(__name__)
api = Api(app)

api_hits = dict()

class Route_List(Resource):
    def get(self, agency_tag):
        global api_hits
        url = "http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=" + agency_tag

        if "routeList" in api_hits:
            api_hits["routeList"] += 1
        else:
            api_hits["routeList"] = 1

        r = requests.get(url)
        return r.content

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

class Route_Config_For_Route_Tag(Resource):
    def get(self, agency_tag, route_tag):
        global api_hits
        url = "http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=" + agency_tag + "&r=" + route_tag

        if "routeConfig" in api_hits:
            api_hits["routeConfig"] += 1
        else:
            api_hits["routeConfig"] = 1

        r = requests.get(url)
        return r.content

class Route_Config_For_Agency_Tag(Resource):
    def get(self, agency_tag):
        global api_hits
        url = "http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=" + agency_tag

        if "routeConfig" in api_hits:
            api_hits["routeConfig"] += 1
        else:
            api_hits["routeConfig"] = 1

        r = requests.get(url)
        return r.content

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

class Route_Predictions_For_Stop_ID_For_Route_Tag(Resource):
    def get(self, agency_tag, stop_id, route_tag):
        global api_hits
        url = "http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=" + agency_tag + "&stopId=" + stop_id + "&routeTag=" + route_tag

        if "predictions" in api_hits:
            api_hits["predictions"] += 1
        else:
            api_hits["predictions"] = 1

        r = requests.get(url)
        return r.content

class Route_Predictions_For_Route_Tag_For_Stop_Tag(Resource):
    def get(self, agency_tag, route_tag, stop_tag):
        global api_hits
        url = "http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=" + agency_tag + "&r=" + route_tag + "&s=" + stop_tag

        print url
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

api.add_resource(Route_List, '/routeList/<agency_tag>')
api.add_resource(Agency_List, '/agencyList')
api.add_resource(Route_Config_For_Route_Tag, '/routeConfig/<agency_tag>/<route_tag>')
api.add_resource(Route_Config_For_Agency_Tag, '/routeConfig/<agency_tag>')
api.add_resource(Route_Predictions_For_Stop_ID, '/predictions/<agency_tag>/<stop_id>')
api.add_resource(Route_Predictions_For_Stop_ID_For_Route_Tag, '/predictions/<agency_tag>/<stop_id>/<route_tag>')
api.add_resource(Route_Predictions_For_Route_Tag_For_Stop_Tag, '/predictions/<agency_tag>/<route_tag>/<stop_tag>')
api.add_resource(API_Hit, '/apiHit/<api_endpoint_name>')

if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0',port=5001)
