# Django
from django.utils.timezone import now


# Today
def get_start_today():
    return now().replace(hour=0, minute=0, second=0, microsecond=0)


def get_end_today():
    return now().replace(hour=23, minute=59, second=59, microsecond=999999)
