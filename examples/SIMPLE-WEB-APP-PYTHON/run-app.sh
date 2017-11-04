docker run -d -p 5001:5001 -e endpoint="routeList" web-app-img:latest
docker run -d -p 5002:5002 -e endpoint="predictionsForMultiStops" web-app-img:latest
docker run -d -p 5003:5003 -e endpoint="schedule" web-app-img:latest
