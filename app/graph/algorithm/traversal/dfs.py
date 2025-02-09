from algorithm.traversal.base import Traversal
from core.graph import Graph
from typing import Any, List, Optional, Set


class DFS(Traversal):
    def traverse(self, graph: Graph, start_node: Any, visited: Optional[Set[Any]] = None) -> List[Any]:
        if visited is None:
            visited = set()

        if start_node not in graph.nodes:
            raise ValueError(f"Node {start_node} not found.")

        visited.add(start_node)
        dfs_order = [start_node]

        for neighbor in graph.get_neighbors(start_node):
            if neighbor not in visited:
                dfs_order.extend(self.traverse(graph, neighbor, visited))

        return dfs_order
