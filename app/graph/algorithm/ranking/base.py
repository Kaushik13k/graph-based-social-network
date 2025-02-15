from abc import ABC, abstractmethod
from core.graph import Graph


class RankingStrategy(ABC):

    @abstractmethod
    def compute_rank(self, graph: Graph):
        pass
