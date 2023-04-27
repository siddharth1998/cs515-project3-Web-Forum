from flask import Flask,request,jsonify
from flask_uuid import FlaskUUID
from uuid import uuid4
from bson.json_util import loads
from pymongo import MongoClient
from mongo_setup import getCollections

import threading
import secrets

from secrets import randbelow

from datetime import timezone

import datetime

app = Flask(__name__)
FlaskUUID(app)


sem = threading.Semaphore()

db = getCollections()

@app.get("/random/<int:sides>")
def roll(sides):
    if sides <= 0:
        return { 'err': 'need a positive number of sides' }, 400
    
    return { 'num': randbelow(sides) + 1 }

def time_bata():
    return datetime.datetime.now(timezone.utc).isoformat()

def get_id(collection_name):
    last_id_data=db[collection_name].find_one(sort=[("id",-1)])
    if last_id_data:
        last_id=last_id_data["id"]
        temp_id=last_id+1
    else:
        temp_id=1   
    
    return temp_id

@app.post("/post")
def post():
    global sem
    if request.method=="POST":
       
       # can be converted into a function which will be used in other methods
        if len((request.json.keys()))>1 or len((request.json.keys()))==0:
            return {"err":"empty body sent"},400 
        if "msg" in request.json:
            pass
        else:
            return {"err":"msg not found"},400
        if type(request.json["msg"])!=str:
            return {"err":"msg value is not a str type"},400
        sem.acquire()
        temp_id=get_id("posts")   
        temp_dict={"id":temp_id,"key":secrets.token_hex(16),"timestamp":time_bata(),"msg":request.json["msg"]}
        db["posts"].insert_one(temp_dict)
        sem.release()
        return {"id":temp_dict["id"],"key":temp_dict["key"],"timestamp":temp_dict["timestamp"]},200
    else:
        return {"err":"Parameters Not Inclucded or this resource not found"},404
    


@app.get("/post/<int:input_id>")
def get(input_id):
    global sem

    if request.method=="GET":
        temp_dict=db["posts"].find_one({"id":input_id})
        if not temp_dict:
            return {"err":"id not found"},404
        else:
            res={"id":input_id,"timestamp":temp_dict["timestamp"],"msg":temp_dict["msg"]}
            return res,200

@app.delete("/post/<int:input_id>/delete/<string:input_key>")
def delete(input_id,input_key):
    global sem
    if request.method=="DELETE":
        
        temp_dict=db["posts"].find_one({"id":input_id})
        if not temp_dict:
            return {"err":"id not found"},404
        else:
            if temp_dict["key"]==input_key:
               sem.acquire()
               db["posts"].delete_one({"id":input_id})
               sem.release()
               return {"id":input_id,"key":temp_dict["key"],"timestamp":temp_dict["timestamp"]}
            else:
                return {"err":"forbidden"},403 
        
@app.post('/user')
def save_user():
    user_json = request.json
    db['users'].insert_one(user_json)
    user_json['_id'] = str(user_json['_id'])
    return {'message': 'User saved successfully!', 'user_id': user_json}, 200

@app.get('/user/<uuid:id>')
def get_user(id):
    user = db['users'].find_one({ '_id': id })
    print(user, type(user))
    return loads(user), 200

