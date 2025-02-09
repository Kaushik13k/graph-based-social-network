from abc import ABC, abstractmethod
from app.graph.core.graph import Graph
from typing import Any, Dict


class RecommendationStrategy(ABC):
    @abstractmethod
    def recommend(self, graph: Graph, user: Any) -> Dict[Any, float]:
        pass
