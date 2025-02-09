from core.graph import Graph
from typing import Any, List
from collections import deque
from algorithm.traversal.base import TraversalStrategy


class BFS(TraversalStrategy):

    def traverse(self, graph: Graph, start_node: Any) -> List[Any]:
        if start_node not in graph.nodes:
            raise ValueError(f"Node {start_node} not found.")

        visited = set()
        queue = deque([start_node])
        bfs_order = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                bfs_order.append(node)
                queue.extend(graph.get_neighbors(node))

        return bfs_order
