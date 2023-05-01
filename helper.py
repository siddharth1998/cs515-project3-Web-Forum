from datetime import timezone

import datetime


def time_bata():
    return datetime.datetime.now(timezone.utc).isoformat()


def get_date_from_iso_str(iso_string):
    return datetime.datetime.fromisoformat(iso_string);


def remove_unnecessary_keys(user_json):
    keys = ['username', 'firstName', 'lastName']
    user_json_copy = dict(user_json)
    for key in user_json_copy.keys():
        if key not in keys:
            user_json.pop(key)

