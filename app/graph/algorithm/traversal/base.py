from abc import ABC, abstractmethod
from app.custom_graph.core.graph import Graph
from typing import Any, List


class TraversalStrategy(ABC):

    @abstractmethod
    def traverse(self, graph: Graph, start_node: Any) -> List[Any]:
        pass
