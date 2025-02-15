from abc import ABC, abstractmethod
from core.graph import Graph
from typing import Any, List


class ShortestPath(ABC):
    @abstractmethod
    def traverse(self, graph: Graph, start_node: Any) -> List[Any]: ...
