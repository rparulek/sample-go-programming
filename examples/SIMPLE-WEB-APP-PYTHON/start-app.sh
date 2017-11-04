docker run -d -p 5001:5001 -e endpoint="routeList" web-app-img:latest
docker run -d -p 5002:5002 -e endpoint="predictionsForMultiStops" web-app-img:latest
docker run -d -p 5003:5003 -e endpoint="schedule" web-app-img:latest
docker run -d -p 5004:5004 -e endpoint="vehicleLocations" web-app-img:latest
docker run -d -p 5005:5005 -e endpoint="messages" web-app-img:latest
docker run -d -p 5006:5006 -e endpoint="predictions" web-app-img:latest
docker run -d -p 5007:5007 -e endpoint="routeConfig" web-app-img:latest
