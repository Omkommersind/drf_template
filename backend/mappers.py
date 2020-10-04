from backend.errors.errors import Errors
from backend.errors.http_exception import HttpException
from backend.entities import PagingOptions, DateTimeFilter
from backend.utils import millis_to_datetime


class RequestToPagingOptionsMapper:
    @staticmethod
    def map(data):
        options = PagingOptions()

        if data.get('offset') is None:
            options.offset = 0
        else:
            try:
                options.offset = int(data.get('offset'))
            except:
                options.offset = 0

        if data.get('limit') is None:
            options.limit = 10
        else:
            try:
                options.limit = options.offset + int(data.get('limit'))
            except:
                options.limit = 10

        return options


class RequestToDateTimeFilterMapper:
    @staticmethod
    def map(data):
        options = DateTimeFilter()

        dt_from = data.get('dt_from')
        if dt_from is not None:
            try:
                options.dt_from = millis_to_datetime(int(dt_from))
            except Exception as ex:
                raise HttpException(detail=ex, status_code=Errors.BAD_REQUEST)

        dt_to = data.get('dt_to')
        if dt_to is not None:
            try:
                options.dt_to = millis_to_datetime(int(dt_to))
            except Exception as ex:
                raise HttpException(detail=ex, status_code=Errors.BAD_REQUEST)

        return options
