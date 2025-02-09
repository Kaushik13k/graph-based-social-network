from typing import Any


class Edge:
    def __init__(self, from_node: Any, to_node: Any, weight: float = 1.0, **attributes):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
        self.attributes = attributes

    def update_attributes(self, **new_attributes):
        self.attributes.update(new_attributes)

    def __repr__(self):
        return f"Edge({self.from_node} -> {self.to_node}, weight={self.weight}, attributes={self.attributes})"

    def __eq__(self, other):
        return (
            isinstance(other, Edge)
            and self.from_node == other.from_node
            and self.to_node == other.to_node
            and self.weight == other.weight
        )

    def __hash__(self):
        return hash((self.from_node, self.to_node))
