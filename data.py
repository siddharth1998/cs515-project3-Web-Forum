import secrets
from helper import time_bata

def generate_user_id():
    return 1

def create_user_db(db, username):
    try:
        key = secrets.token_hex(32)
        id = generate_user_id()

        err = False
        existingUser = db['users'].find_one({ 'username': username })
        if existingUser:
            err = True
            err, 400, { 'message': 'username not available' }
        else:
            newUser = db['users'].insert_one(dict({ 'key': key, 'id': id, 'username': username }))
            if newUser:
                err, 200, newUser
            else:
                err = True
                err, 500, { 'message': 'Unable to create the user' }
    except Exception as e:
        print(e)
        return True, 500, { 'message': 'Internal server error' }
    
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