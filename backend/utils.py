import datetime
import json
from json import JSONDecodeError

import pytz
from djangorestframework_camel_case.util import underscoreize

from backend.errors.errors import Errors
from backend.errors.http_exception import HttpException


def get_body_in_request(request):
    if not request.body:
        raise HttpException(detail=Errors.BAD_REQUEST.name, status_code=Errors.BAD_REQUEST)
    try:
        data = json.loads(request.body.decode('utf-8'))
        return underscoreize(data)
    except JSONDecodeError:
        data = request.POST
        return underscoreize(data)


def choices(em):
    return [(e.value, e.name) for e in em]


def millis_to_datetime(millis):
    dt = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=millis / 1000.0)
    return dt.replace(tzinfo=pytz.utc)


def millis_to_date(millis):
    return datetime.date.fromtimestamp(millis / 1000.0)


def date_to_millis(date):
    try:
        return int(datetime.datetime.combine(date, datetime.time.min).timestamp()) * 1000
    except:
        return None


def get_timestamp_in_millis(dt):
    try:
        return (dt.timestamp() * 1000).__int__()
    except:
        return None


def get_current_dt_in_timestamp():
    return get_timestamp_in_millis(datetime.datetime.now())


def datetime_to_millis(dt):
    try:
        return int(datetime.datetime.timestamp(dt)) * 1000
    except:
        return None
