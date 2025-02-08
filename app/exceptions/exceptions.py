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
