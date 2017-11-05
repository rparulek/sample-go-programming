docker run -d -p 5001:5001 -e endpoint="agencyList" docker/next-bus-api:v1.0.0
docker run -d -p 5002:5002 -e endpoint="routeList" docker/next-bus-api:v1.0.0
docker run -d -p 5003:5003 -e endpoint="routeConfig" docker/next-bus-api:v1.0.0
docker run -d -p 5004:5004 -e endpoint="predictions" docker/next-bus-api:v1.0.0
docker run -d -p 5005:5005 -e endpoint="predictionsForMultiStops" docker/next-bus-api:v1.0.0
docker run -d -p 5006:5006 -e endpoint="schedule" docker/next-bus-api:v1.0.0
docker run -d -p 5007:5007 -e endpoint="vehicleLocations" docker/next-bus-api:v1.0.0
docker run -d -p 5008:5008 -e endpoint="messages" docker/next-bus-api:v1.0.0
