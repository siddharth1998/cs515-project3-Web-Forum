import datetime
import re


class ValidationError(Exception):
    def __init__(self, status, message):
        self.type = status
        self.message = message
        super().__init__(self.message)


class InternalError(Exception):
    def __init__(self, status, message):
        self.type = status
        self.message = message
        super().__init__(self.message)


def validate_username(username):
    if (len(username) < 5) or (len(username) > 30):
        raise ValidationError(400, { 'message': 'username needs a minimum length of 5 to 30 characters' })

    if not re.match("^[a-zA-Z0-9_.-]+$", username):
        raise ValidationError(400, { 'message': 'username can have only letters, digits, underscore, . or - characters' })


def validate_name(key, name):
    if (len(name) < 5) or (len(name) > 30):
        raise ValidationError(400, { 'message': f'{key} needs to be between the length of 5 to 30 characters' })

    if not re.match("^[a-zA-Z ]+$", name):
        raise ValidationError(400, { 'message': f'{key} can have only letters, digits, underscore, . or - characters' })


def validate_user_id(id):
    if (len(id) < 16) or (len(id) > 16):
        raise ValidationError(400, {'message': 'The user id is invalid' })


def validate_user_key(key):
    if (len(key) < 24) or (len(key) > 24):
        raise ValidationError(400, {'message': 'The user key is invalid' })


def create_user_validation(user_json):
    validate_username(user_json.get('username', '?'))


def update_user_validation(user_json):
    if 'key' not in user_json:
        raise ValidationError(400, {'message': 'user key required to make changes to user metadata'})
    validate_user_key(user_json.get('key', '?'))
    validate_username(user_json.get('username', '?'))
    validate_name('firstName', user_json.get('firstName', '?'))
    validate_name('lastName', user_json.get('lastName', '?'))


def get_user_validation(id):
    validate_user_id(id)


def search_user_validation(user_json):
    if 'username' in user_json: validate_username(user_json.get('username'))
    if 'firstName' in user_json: validate_name('firstName', user_json.get('firstName', '?'))
    if 'lastName' in user_json: validate_name('lastName', user_json.get('lastName', '?'))


def datetime_validation(dt_str):
    try: datetime.datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
    except Exception: raise ValidationError(400, {'message': 'date is not of valid format'})


def user_id_exist_checker(db,request):
    user_data=db["users"].find_one({"id":request.json["user_id"]})
    if user_data:
        return False,None, 200
    else:
        return True, {"err":"The user dose not exists sending"},404

def create_post_validation(db,request):
    if len((request.json.keys()))>3  or len((request.json.keys()))==0:
            return True,{"err":"empty body sent"},400 
    if "user_id" in request.json.keys():
        is_error,message,status_code=user_id_exist_checker(db,request)
        if is_error:
            return True, message, status_code
    if "msg" in request.json:
        is_error,message,status_code=validation_user_request(db,request)
        if is_error:
            return True,message,status_code
    else:
        return True,{"err":"msg not found"},400
    if type(request.json["msg"])!=str:
        return True,{"err":"msg value is not a str type"},400
    return False,None,200


def validation_user_request(db,request):
    user_id=False
    if "user_id" in request.json:
        if "key" not in request.json:
            return True,{"err":"user_id given without key"},400
        user_id=True
    elif "key" in request.json:
        if "user_id" not in request.json:
            return True,{"err":"key given without user_id"},400
        user_id=True
    for i in request.json.keys():
        if i not in ["msg","user_id","key"]:
            return True,{"err":"Unknow parameters given"},400
    if user_id:
        if (db["users"].find_one({"id":request.json["user_id"],"key":request.json["key"]})):
            return False,None,200
        else:
            return True,{"err":"user_id and key should be of the same user"},403
    else:
        pass
    return False,None,200
