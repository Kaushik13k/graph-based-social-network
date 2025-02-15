from algorithm.ranking.base import RankingStrategy
from core.graph import Graph


class HITS(RankingStrategy):

    def __init__(self, iterations: int = 10):
        self.iterations = iterations

    def compute_rank(self, graph: Graph) -> tuple[dict, dict]:
        hubs = {node: 1.0 for node in graph.nodes}
        authorities = {node: 1.0 for node in graph.nodes}

        for _ in range(self.iterations):
            for node in graph.nodes:
                authorities[node] = sum(hubs[neighbor]
                                        for neighbor in graph.get_neighbors(node))

            for node in graph.nodes:
                hubs[node] = sum(authorities[neighbor]
                                 for neighbor in graph.get_neighbors(node))

            max_auth = max(authorities.values()) or 1.0
            max_hub = max(hubs.values()) or 1.0

            for node in authorities:
                authorities[node] /= max_auth

            for node in hubs:
                hubs[node] /= max_hub

        return hubs, authorities
