#!/bin/sh

echo "Running the setup.sh"

service mongod status

apt-get install gnupg -y

apt install curl -y

curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \
   gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
   --dearmor

touch /etc/apt/sources.list.d/mongodb-org-6.0.list

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list

apt-get update

apt-get install -y mongodb-org

mkdir -p /data/db

mongod --fork --syslog

location_of_python=$(which python3)

echo $location_of_python

# apt install python3-pip -y
#above python pip can be removed if professor answers it 

pip3 install -r requirement.txt

# $location_of_python -m flask run 