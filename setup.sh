#!/bin/sh

sudo apt-get install gnupg

sudo apt install curl -y

curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
   --dearmor

sudo touch /etc/apt/sources.list.d/mongodb-org-6.0.list

sudo echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

sudo apt-get update

sudo apt-get install -y mongodb-org

sudo systemctl daemon-reload


sudo systemctl start mongod

sudo systemctl enable mongod

location_of_python=$(which python3)

echo $location_of_python

apt install python3-pip -y
#above python pip can be removed if professor answers it 

pip3 install -r requirement.txt

$location_of_python -m flask run 
