from algorithm.traversal.bfs import BFS
from algorithm.traversal.dfs import DFS
from algorithm.traversal.dijkstra import Dijkstra


class TraversalFactory:

    @staticmethod
    def get_traversal_algorithm(algorithm_type: str):
        if algorithm_type.lower() == "bfs":
            return BFS()
        elif algorithm_type.lower() == "dfs":
            return DFS()
        elif algorithm_type.lower() == "dijkstra":
            return Dijkstra()
        else:
            raise ValueError(f"Unknown traversal algorithm: {algorithm_type}")
