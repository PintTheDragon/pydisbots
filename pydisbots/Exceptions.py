
class APIError(Exception):
    def __init__(self, debug):
        self.debug = debug

    def __str__(self):
        return f'An exception with the API occurred - Debug: {debug}'

class BotNotFound(Exception):
    def __init__(self, uid: int):
        self.uid = uid

    def __str__(self):
        return f'404 Bot {uid} not found'

class UserNotFound(Exception):
    def __init__(self, uid: int):
        self.uid = uid

    def __str__(self):
        return f'404 User {uid} not found'
