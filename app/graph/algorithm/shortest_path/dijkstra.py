import heapq
from core.graph import Graph
from typing import Any, Dict, Tuple, List
from algorithm.shortest_path.base import ShortestPath


class Dijkstra(ShortestPath):
    def traverse(self, graph: Graph, start_node: Any) -> Dict[Any, Tuple[float, List[Any]]]:
        if start_node not in graph.nodes:
            raise ValueError(f"Node {start_node} not found.")

        priority_queue = [(0, start_node, [])]
        shortest_paths = {node: (float('inf'), []) for node in graph.nodes}
        shortest_paths[start_node] = (0, [start_node])

        while priority_queue:
            current_distance, current_node, path = heapq.heappop(
                priority_queue)

            if current_distance > shortest_paths[current_node][0]:
                continue

            for neighbor, weight in graph.get_neighbors(current_node):
                distance = current_distance + weight

                if distance < shortest_paths[neighbor][0]:
                    shortest_paths[neighbor] = (distance, path + [neighbor])
                    heapq.heappush(priority_queue, (distance,
                                   neighbor, path + [neighbor]))

        return shortest_paths
