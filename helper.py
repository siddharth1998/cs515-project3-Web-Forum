from datetime import timezone

import datetime


def time_bata():
    return datetime.datetime.now(timezone.utc).isoformat()