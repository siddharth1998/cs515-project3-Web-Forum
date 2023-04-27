#!/bin/sh

 wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add - 

 sudo apt-get install gnupg 

 wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add - 

 lsb_release -dc. 

 echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list 

 sudo apt-get update 

 sudo apt-get install -y mongodb-org 

 mongo --eval 'db.runCommand({ connectionStatus: 1 })' 