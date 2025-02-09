from algorithm.ranking.base import RankingStrategy
from app.custom_graph.core.graph import Graph


class PageRank(RankingStrategy):

    def __init__(self, damping_factor: float = 0.85, iterations: int = 10):
        self.damping_factor = damping_factor
        self.iterations = iterations

    def compute_rank(self, graph: Graph) -> dict:

        num_nodes = len(graph.nodes)
        if num_nodes == 0:
            return {}

        ranks = {node: 1 / num_nodes for node in graph.nodes}

        for _ in range(self.iterations):
            new_ranks = {}
            for node in graph.nodes:
                incoming_links = [
                    n for n in graph.nodes if node in graph.get_neighbors(n)]
                new_rank = (1 - self.damping_factor) / num_nodes
                new_rank += self.damping_factor * sum(
                    ranks[n] / len(graph.get_neighbors(n)) for n in incoming_links if graph.get_neighbors(n)
                )
                new_ranks[node] = new_rank
            ranks = new_ranks

        return ranks
