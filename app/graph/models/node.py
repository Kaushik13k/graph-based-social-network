from typing import Any, Dict


class Node:
    def __init__(self, node_id: Any, node_type: str = "default", **attributes: Dict[str, Any]):
        self.node_id = node_id
        self.node_type = node_type
        self.attributes = attributes

    def __repr__(self):
        return f"Node(id={self.node_id}, type={self.node_type}, attributes={self.attributes})"

    def __eq__(self, other):
        return (
            isinstance(other, Node)
            and self.node_id == other.node_id
            and self.node_type == other.node_type
            and self.attributes == other.attributes
        )

    def __hash__(self):
        return hash((self.node_id, self.node_type, frozenset(self.attributes.items())))

    def update_attributes(self, **new_attributes):
        self.attributes.update(new_attributes)
