import re

def create_user_validation(user_json):
    if len(user_json.get('username', '')) < 5:
        return True, 400, { 'message': 'Username needs a minimum length of 5 characters' }

    if not re.match("^[a-zA-Z0-9_.-]+$", user_json.get('username', '?')):
        return True, 400, { 'message': 'Username can have only letters, digits, underscore, . or - characters' }
    
    return False, '', ''
