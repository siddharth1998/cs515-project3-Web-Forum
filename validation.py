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
        raise ValidationError(400, { 'message': f'{key} needs a between length of 5 to 30 characters' })

    if not re.match("^[a-zA-Z ]+$", name):
        raise ValidationError(400, { 'message': f'{key} can have only letters, digits, underscore, . or - characters' })


def validate_user_id(id):
    if (len(id) < 16) or (len(id) > 16):
        raise ValidationError(400, {'message': 'The user id is invalid' })


def create_user_validation(user_json):
    validate_username(user_json.get('username', '?'))


def update_user_validation(user_json):
    validate_username(user_json.get('username', '?'))
    validate_name('firstName', user_json.get('firstName', '?'))
    validate_name('lastName', user_json.get('lastName', '?'))


def get_user_validation(id):
    validate_user_id(id)


def search_user_validation(user_json):
    if 'username' in user_json: validate_username(user_json.get('username'))
    if 'firstName' in user_json: validate_name('firstName', user_json.get('firstName', '?'))
    if 'lastName' in user_json: validate_name('lastName', user_json.get('lastName', '?'))

def create_post_validation(db,request):
    if len((request.json.keys()))>3  or len((request.json.keys()))==0:
            return True,{"err":"empty body sent"},400 
    if "msg" in request.json:
        is_error,message,status_code=validation_user_request(db,request)
        if is_error:
            return True,message,status_code
    else:
        return True,{"err":"msg not found"},400
    if type(request.json["msg"])!=str:
        return True,{"err":"msg value is not a str type"},400
    return False,None,200

# def post_exsisting(db,input_id,input_key):
#     temp_dict=db["posts"].find_one({"id":input_id})
#     if not temp_dict:
#         return True,{"err":"id not found"},404
#     else:
#         if temp_dict["key"]==input_key:
#             return False,None,200


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
