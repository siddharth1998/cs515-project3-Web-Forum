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
    validate_name(user_json.get('firstName', '?'))
    validate_name(user_json.get('lastName', '?'))


def get_user_validation(id):
    validate_user_id(id)


def search_user_validation(user_json):
    if 'username' in user_json: validate_username(user_json.get('username'))
    if 'firstName' in user_json: validate_name(user_json.get('firstName'))
    if 'lastName' in user_json: validate_name(user_json.get('lastName'))


