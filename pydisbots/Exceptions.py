
class APIError(Exception):
    def __init__(self, debug):
        self.debug = debug

    def __str__(self):
        return f'An exception with the API occurred - Debug: {self.debug}'

class BotNotFound(Exception):
    def __init__(self, bot):
        self.bot = bot

    def __str__(self):
        return f'404 Bot {self.bot} not found'

class InvalidBot(Exception):
    def __init__(self, bot):
        self.bot = bot

    def __str__(self):
        return f'Bot {self.bot} is invalid'

class UserNotFound(Exception):
    def __init__(self, uid: int):
        self.uid = uid

    def __str__(self):
        return f'404 User {self.uid} not found'

class InvalidUser(Exception):
    def __init__(self, uid: int):
        self.uid = uid

    def __str__(self):
        return f'User {self.uid} is invalid'

class UnauthorizedError(Exception):
    def __str__(self):
        return '401 Unauthorized (Your secret is invalid)'
