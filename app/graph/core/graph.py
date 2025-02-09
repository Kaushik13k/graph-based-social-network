from typing import Any, Dict, List
from models.node import Node
from models.edge import Edge
from observer import GraphObserver
from exceptions.exceptions import NodeNotFoundError, EdgeAlreadyExistsError, NodeAlreadyExistsError


class Graph:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Graph, cls).__new__(cls)
            cls._instance.nodes = dict()
            cls._instance.adjacency_list = dict()
            cls._instance.observer = GraphObserver()
        return cls._instance

    def add_node(self, node_id: Any, node_type: str = "default", **attributes) -> None:
        if node_id in self.nodes:
            raise NodeAlreadyExistsError(f"Node {node_id} already exists.")
        self.nodes[node_id] = Node(node_id, node_type, **attributes)
        self.adjacency_list[node_id] = list()
        self.observer.notify(f"Node {node_id} of type {node_type} added.")

    def add_edge(self, from_node: Any, to_node: Any, weight: float = 1.0) -> None:
        if from_node not in self.nodes or to_node not in self.nodes:
            raise NodeNotFoundError(
                f"Node {from_node} or {to_node} not found.")

        edge = Edge(from_node, to_node, weight)
        if edge in self.adjacency_list[from_node]:
            raise EdgeAlreadyExistsError(f"Edge {edge} already exists.")

        self.adjacency_list[from_node].append(edge)
        self.observer.notify(
            f"Edge added from {from_node} to {to_node} with weight {weight}.")

    def get_neighbors(self, node_id: Any) -> List[Any]:
        return [edge.to_node for edge in self.adjacency_list[node_id]]

    def print_graph(self) -> None:
        for node_id, edges in self.adjacency_list.items():
            neighbors = [edge.to_node for edge in edges]
            print(f"Node {node_id} -> {neighbors}")

    def __repr__(self) -> str:
        return f"Graph(nodes={list(self.nodes.keys())})"
