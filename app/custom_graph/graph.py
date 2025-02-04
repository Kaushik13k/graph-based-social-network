from custom_graph.edge import Edge
from custom_graph.node import Node
from typing import Any, Dict, List, Optional
from custom_graph.exceptions import NodeNotFoundError, EdgeAlreadyExistsError, NodeAlreadyExistsError

# TODO: Implement the leftout's


class Graph:
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.nodes: Dict[Any, Node] = dict()
        self.adjacency_list: Dict[Any, List[Edge]] = dict()
        self._node_attrs: Dict[Any, Node] = dict()

    def add_node(self, node_id: Any, **attr) -> None:
        if node_id in self.nodes:
            raise NodeAlreadyExistsError(
                f"Node {node_id} already exists in the graph.")
        if node_id is None:
            raise ValueError("None cannot be a node")

        self.nodes[node_id] = Node(node_id, **attr)
        self.adjacency_list[node_id] = list()
        self._node_attrs[node_id] = dict()

        # Update or set node attributes
        self._node_attrs[node_id].update(attr)

    def number_of_nodes(self):
        pass

    def order(self):
        pass

    def remove_node(self):
        pass

    def has_node(self):
        pass

    def add_edge(self, from_node: Any, to_node: Any, weight: Optional[float] = 1.0) -> None:
        if from_node not in self.nodes or to_node not in self.nodes:
            raise NodeNotFoundError(
                f"Node {from_node} or {to_node} not found in the graph.")
        edge = Edge(from_node, to_node, weight)
        if edge in self.adjacency_list[from_node]:
            raise EdgeAlreadyExistsError(
                f"Edge {edge} already exists in the graph.")

        self.adjacency_list[from_node].append(edge)
        if not self.directed:
            self.adjacency_list[to_node].append(
                Edge(to_node, from_node, weight))

    def remove_edge(self):
        pass

    def has_edge(self):
        pass

    def get_neighbors(self, node_id: Any) -> List[Any]:
        if node_id not in self.nodes:
            raise NodeNotFoundError(f"Node {node_id} not found in the graph.")
        return [edge.to_node for edge in self.adjacency_list[node_id]]

    def __repr__(self) -> str:
        return f"Graph(directed={self.directed}, nodes={list(self.nodes.keys())})"
