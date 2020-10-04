import types
from datetime import datetime
from django.utils import timezone

methods = (types.FunctionType, types.MethodType)


class BaseEntity:
    def __init__(self):
        pass

    def get_kwargs(self):
        kwargs = {}
        for key, value in self.__dict__.items():
            if not isinstance(value, methods) and value is not None:
                kwargs[key] = value
        return kwargs


class PagingOptions:
    def __init__(self):
        self.limit = 10
        self.offset = 0


class DateTimeFilter:
    def __init__(self):
        self.dt_from = datetime.min
        self.dt_to = timezone.now()
