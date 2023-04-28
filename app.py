from flask import Flask, request
from flask_uuid import FlaskUUID
from mongo_setup import getCollections
from validation import create_user_validation, update_user_validation, get_user_validation, search_user_validation, ValidationError, InternalError, create_post_validation
from data import create_user_db, update_user_db, get_user_db, find_user_db, get_id, create_post_db, get_post_db, \
    get_post_by_date_range

import threading

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
    try:
        user_json = request.json
        create_user_validation(user_json)

        success, status, resp = create_user_db(db, user_json.get('username', ''))
        return resp, status
    except (ValidationError, InternalError) as err:
        return err.message, err.type
    except Exception as e:
        return {'message': 'Internal server error'}, 500


@app.put('/user')
def update_user():
    try:
        user_json = request.json
        update_user_validation(user_json)
        success, status, resp = update_user_db(db, user_json['key'], user_json)
        return resp, status
    except (ValidationError, InternalError) as err:
        return err.message, err.type
    except Exception:
        return {'message': 'Internal server error'}, 500


@app.get('/user/<id>')
def get_user(id):
    try:
        get_user_validation(id)
        success, status, resp = get_user_db(db, id)
        return resp, status
    except (ValidationError, InternalError) as err:
        return err.message, err.type
    except Exception as e:
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


@app.get('/post/date-range')
def date_based_filter():
    try:
        filter_json = request.json
        return get_post_by_date_range(db, filter_json), 200
    except (ValidationError, InternalError) as err:
        return err.message, err.type
    except Exception as e:
        return {'message': 'Internal server error'}, 500

