import secrets
from validation import ValidationError, InternalError
from helper import time_bata
import datetime


def create_user_db(db, username):
    key = secrets.token_hex(12)
    id = secrets.token_hex(8)
    user_dict = { 'key': key, 'id': id, 'username': username }

    existing_user = db['users'].find_one({ 'username': username }, { '_id': 0 })
    print('user', existing_user)
    if existing_user:
        raise ValidationError(400, { 'message': 'username not available' })
    else:
        new_user = db['users'].insert_one(user_dict)
        if new_user:
            user_dict.pop('_id')
            return True, 200, user_dict
        else:
            raise ValidationError(500, { 'message': 'Unable to create the user' })


def update_user_db(db, key, user_json):
    existing_user = db['users'].find_one({ 'key': key })
    if existing_user:
        updated_user = db['users'].find_one_and_update({ 'key': key }, user_json, { '_id': 0 })
        print('update user', updated_user)
        # TODO: Check the value of updated_user
        if updated_user:
            return True, 200, { 'message': 'Updated user metadata successfully' }
        else:
            raise InternalError(400, {'message': 'Unable to update the record'})
    else:
        raise ValidationError(404, { 'message': 'User does not exist' })


def get_user_db(db, id):
    existing_user = db['users'].find_one({ 'id': id }, { '_id': 0 })
    if existing_user:
        return True, 200, existing_user
    else:
        raise ValidationError(404, { 'message': 'User does not exist' })


def find_user_db(db, user_json):
    existing_user = db['users'].find_one(user_json, { '_id': 0 })
    if existing_user:
        return True, 200, existing_user
    else:
        raise ValidationError(404, { 'message': 'User does not exist' })
    
def get_id(db,collection_name):
    last_id_data=db[collection_name].find_one(sort=[("id",-1)])
    if last_id_data:
        last_id=last_id_data["id"]
        temp_id=last_id+1
    else:
        temp_id=1   
    
    return temp_id

def create_post_db(db,request):
    temp_id=get_id(db,"posts")   
    # iso_time=
    # d = datetime.datetime.strptime(iso_time, "%Y-%m-%dT%H:%M:%S.000Z")
    temp_dict={"id":temp_id,"key":secrets.token_hex(16),"timestamp":time_bata(),"msg":request.json["msg"]}
    db["posts"].insert_one(temp_dict)
    return temp_dict

def get_post_db(db,input_id):
    temp_dict=db["posts"].find_one({"id":input_id})
    if not temp_dict:
        return True,{"err":"id not found"},404
    else:
        res={"id":input_id,"timestamp":temp_dict["timestamp"],"msg":temp_dict["msg"]}
        return False,res,200
    
def delete_post_db(db,input_id,input_key):
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
