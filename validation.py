import re

def create_user_validation(user_json):
    if len(user_json.get('username', '')) < 5:
        return True, 400, { 'message': 'Username needs a minimum length of 5 characters' }

    if not re.match("^[a-zA-Z0-9_.-]+$", user_json.get('username', '?')):
        return True, 400, { 'message': 'Username can have only letters, digits, underscore, . or - characters' }
    
    return False, '', ''

def create_post_validation(request):
    if len((request.json.keys()))>1 or len((request.json.keys()))==0:
            return True,{"err":"empty body sent"},400 
    if "msg" in request.json:
        pass
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