class NodeNotFoundError(Exception):
    """Raised when a node is not found in the graph."""

    def __init__(self, msg: str = None):
        super().__init__(msg)


class NodeAlreadyExistsError(Exception):
    """Raised when an node already exists in the graph."""

    def __init__(self, msg: str = None):
        super().__init__(msg)


class EdgeAlreadyExistsError(Exception):
    """Raised when an edge already exists in the graph."""

    def __init__(self, msg: str = None):
        super().__init__(msg)


class EdgeNotFoundError(Exception):
    """Raised when a edge is not found in the graph."""

    def __init__(self, msg: str = None):
        super().__init__(msg)
