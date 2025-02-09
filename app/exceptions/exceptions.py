class UserNotFoundException(Exception):
    def __init__(self, msg: str = None):
        super().__init__(msg)


class UserAlreadyExistsException(Exception):
    def __init__(self, msg: str = None):
        super().__init__(msg)


class PostNotFoundException(Exception):
    def __init__(self, msg: str = None):
        super().__init__(msg)


class PostAlreadyExistsException(Exception):
    def __init__(self, msg: str = None):
        super().__init__(msg)


class UserNotFoundError(Exception):
    def __init__(self, username: str):
        self.message = f"User '{username}' not found in the system."
        super().__init__(self.message)


class MessageEncryptionError(Exception):
    def __init__(self, action: str):
        self.message = f"Error occurred while {action} the message."
        super().__init__(self.message)


class DatabaseQueryError(Exception):
    def __init__(self, query: str):
        self.message = f"Database query failed: {query}"
        super().__init__(self.message)
