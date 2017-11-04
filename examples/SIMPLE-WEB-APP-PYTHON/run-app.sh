docker run -d -p 5001:5001 -e endpoint="routeList" test-img
docker run -d -p 5002:5002 -e endpoint="predictionsForMultiStops" test-img
