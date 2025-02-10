from typing import Any, Dict, List
from graph.models.node import Node
from graph.models.edge import Edge
from graph.core.base import GraphBase
from graph.core.observer import GraphObserver, UserNotification
from graph.exceptions.exceptions import NodeNotFoundError, EdgeAlreadyExistsError, NodeAlreadyExistsError


class Graph(GraphBase):

    def __init__(self, directed=False):
        self.nodes = dict()
        self.adjacency_list = dict()
        self.directed = directed
        self.observer = GraphObserver()
        self.observer.attach(UserNotification())

    def add_node(self, node_id: Any, node_type: str = "default", **attributes) -> None:
        if node_id in self.nodes:
            raise NodeAlreadyExistsError(f"Node {node_id} already exists.")
        self.nodes[node_id] = Node(node_id, node_type, **attributes)
        self.adjacency_list[node_id] = list()
        self.observer.notify(f"Node {node_id} of type {node_type} added.")

    def remove_node(self, node_id: Any) -> None:
        if node_id not in self.nodes:
            raise NodeNotFoundError(f"Node {node_id} not found.")

        del self.nodes[node_id]
        del self.adjacency_list[node_id]

        for edges in self.adjacency_list.values():
            edges[:] = [edge for edge in edges if edge.to_node != node_id]

        self.observer.notify(f"Node {node_id} removed.")

    def add_edge(self, from_node: Any, to_node: Any, weight: float = 1.0, **attributes) -> None:
        if from_node not in self.nodes or to_node not in self.nodes:
            raise NodeNotFoundError(
                f"Node {from_node} or {to_node} not found.")

        edge = Edge(from_node, to_node, weight, **attributes)
        if edge in self.adjacency_list[from_node]:
            raise EdgeAlreadyExistsError(f"Edge {edge} already exists.")

        self.adjacency_list[from_node].append(edge)

        if not self.directed:
            reverse_edge = Edge(to_node, from_node, weight, **attributes)
            self.adjacency_list[to_node].append(reverse_edge)

        self.observer.notify(
            f"Edge added from {from_node} to {to_node} with weight {weight} and attributes {attributes}.")

    def remove_edge(self, from_node: Any, to_node: Any) -> None:
        if from_node not in self.adjacency_list:
            raise NodeNotFoundError(f"Node {from_node} not found.")

        initial_length = len(self.adjacency_list[from_node])
        self.adjacency_list[from_node] = [
            edge for edge in self.adjacency_list[from_node] if edge.to_node != to_node]

        if not self.directed:
            self.adjacency_list[to_node] = [
                edge for edge in self.adjacency_list[to_node] if edge.to_node != from_node]

        if len(self.adjacency_list[from_node]) < initial_length:
            self.observer.notify(
                f"Edge removed from {from_node} to {to_node}.")
        else:
            raise NodeNotFoundError(
                f"Edge from {from_node} to {to_node} does not exist.")

    def update_edge_weight(self, from_node: Any, to_node: Any, new_weight: float) -> None:
        for edge in self.adjacency_list[from_node]:
            if edge.to_node == to_node:
                edge.weight = new_weight
                self.observer.notify(
                    f"Updated edge weight from {from_node} to {to_node} to {new_weight}.")
                return

        raise NodeNotFoundError(
            f"Edge from {from_node} to {to_node} not found.")

    def get_neighbors(self, node_id: Any) -> List[Any]:
        if node_id not in self.adjacency_list:
            raise NodeNotFoundError(f"Node {node_id} not found.")
        return [edge.to_node for edge in self.adjacency_list[node_id]]

    def order(self) -> int:
        return len(self.nodes)

    def degree(self, node_id: Any) -> Dict[str, int]:
        if node_id not in self.nodes:
            raise NodeNotFoundError(f"Node {node_id} not found.")

        out_degree = len(self.adjacency_list[node_id])

        if not self.directed:
            return {"degree": out_degree}

        in_degree = sum(1 for edges in self.adjacency_list.values()
                        for edge in edges if edge.to_node == node_id)

        return {"in-degree": in_degree, "out-degree": out_degree}

    def has_node(self, node_id: Any) -> bool:
        return node_id in self.nodes

    def has_edge(self, from_node: Any, to_node: Any) -> bool:
        return any(edge.to_node == to_node for edge in self.adjacency_list.get(from_node, []))

    def __repr__(self) -> str:
        return f"Graph(nodes={list(self.nodes.keys())})"
