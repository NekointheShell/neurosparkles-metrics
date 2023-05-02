from flask import request


class Error(Exception):
    def __init__(self, message):
        super().__init__(message)


class DataError(Error):
    def __init__(self):
        super().__init__('Invalid data in request from {}'.format(request.remote_addr))


class AuthError(Error):
    def __init__(self):
        super().__init__('Failed login from {}'.format(request.remote_addr))
