from typing import Any


class Node:
    def __init__(self, node_id: Any, **attributes):
        self.node_id = node_id

    def __repr__(self):
        return f"Node(id={self.node_id})"

    def __eq__(self, other):
        return isinstance(other, Node) and self.node_id == other.node_id

    def __hash__(self):
        return hash(self.node_id)
