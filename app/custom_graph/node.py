from typing import Any


class Node:
    def __init__(self, node_id: Any, **attributes):
        self.node_id = node_id
        self.attributes = attributes

    def __setitem__(self, key, value):
        self.attributes[key] = value

    def __getitem__(self, key):
        return self.attributes[key]

    def __repr__(self):
        return f"Node(id={self.node_id}, attributes={self.attributes})"

    def __eq__(self, other):
        return isinstance(other, Node) and self.node_id == other.node_id

    def __hash__(self):
        return hash(self.node_id)
