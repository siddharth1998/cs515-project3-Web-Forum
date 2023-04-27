from flask import Flask, request
from flask_uuid import FlaskUUID
from mongo_setup import getCollections
from validation import create_user_validation, update_user_validation, get_user_validation, search_user_validation, ValidationError, InternalError, create_post_validation
from data import create_user_db, update_user_db, get_user_db, find_user_db, get_id,create_post_db,get_post_db

import threading
import secrets

from secrets import randbelow


app = Flask(__name__)
FlaskUUID(app)

sem = threading.Semaphore()

db = getCollections()




@app.post("/post")
def create_post():
    global sem
    is_error,error_message,status_code=create_post_validation(request)
    if not is_error:
        sem.acquire()
        temp_dict=create_post_db(db,request)
        sem.release()
        return {"id": temp_dict["id"], "key": temp_dict["key"], "timestamp": temp_dict["timestamp"]}, 200
    else:
        return error_message,status_code
    


@app.get("/post/<int:input_id>")
def get_post(input_id):
    global sem

    is_error,res,status_code=get_post_db(db,input_id)
    return res,status_code

@app.delete("/post/<int:input_id>/delete/<string:input_key>")
def delete_post(input_id,input_key):
    global sem
    
        
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
def create_user():
    user_json = request.json
    err, status, resp = create_user_validation(user_json)

    if err: return resp, status

    err1, status1, resp1 = create_user_db(db, user_json.get('username', ''))
    if err1: return resp1, status1


# @app.get('/user/<uuid:id>')
# def get_user(id):
#     user = db['users'].find_one({ '_id': id })
#     print(user, type(user))
#     return loads(user), 200


# def get_user_by_id(user_id):
#     pass

@app.get('/user/<string:id>')
def get_user(id):
    try:
        get_user_validation(id)
        success, status, resp = get_user_db(db, id)
        return resp, status
    except (ValidationError, InternalError) as err:
        return err.message, err.type
    except Exception:
        return {'message': 'Internal server error'}, 500


@app.post('/user/search')
def search_user():
    try:
        user_json = request.json
        search_user_validation(user_json)
        success, status, resp = find_user_db(db, user_json)
        return resp, status
    except (ValidationError, InternalError) as err:
        return err.message, err.type
    except Exception:
        return {'message': 'Internal server error'}, 500


# @app.get('/post/date/find')
# def date_based_filter():
#     try
