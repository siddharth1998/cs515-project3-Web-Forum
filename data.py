import secrets

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