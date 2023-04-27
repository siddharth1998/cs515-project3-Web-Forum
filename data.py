import secrets
from validation import ValidationError, InternalError


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