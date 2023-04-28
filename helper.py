from datetime import timezone

import datetime


def time_bata():
    return datetime.datetime.now(timezone.utc).isoformat()


def get_date_from_iso_str(iso_string):
    return datetime.datetime.fromisoformat(iso_string);

