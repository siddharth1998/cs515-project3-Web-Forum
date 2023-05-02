#!/bin/sh

# echo "Running the run.sh"

# location_of_python=$(which python3)

# $location_of_python -m flask run 

exec flask run -p 5000 &

echo "Running the test.sh"

sleep 3

newman run cs515.postman_collection.json -n 2
newman run users_collection.json -n 2
