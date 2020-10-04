class BaseServerException(Exception):

    def __init__(self, detail, status_code, message):
        super().__init__(message)
        self.detail = detail
        self.status_code = status_code


class EntityDoesNotExistException(BaseServerException):

    def __init__(self):
        super().__init__(detail='entity', status_code=404, message='Entity not found')


class InternalIOException(BaseServerException):
    def __init__(self):
        super().__init__(detail='In out internal server exception', status_code=404,
                         message='In out internal server exception')


class TagLengthException(BaseServerException):
    def __init__(self, tag: str):
        msg = 'Tag: %s, length: %d, max_length: 32' % (tag, len(tag))
        super().__init__(detail=msg, status_code=404, message='Tag is too long, ' + msg)
