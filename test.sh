#!/bin/sh

echo "Running the test.sh"

newman run users_collection.json -n 1

