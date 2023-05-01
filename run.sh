#!/bin/sh

echo "Running the run.sh"

# location_of_python=$(which python3)

# $location_of_python -m flask run 

exec flask run -p 5000 &