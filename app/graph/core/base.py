from abc import ABC, abstractmethod
from typing import Any, List


class GraphBase(ABC):
    @abstractmethod
    def add_node(self, node_id: Any, node_type: str = "default", **
                 attributes): ...

    @abstractmethod
    def remove_node(self, node_id: Any): ...

    @abstractmethod
    def add_edge(self, from_node: Any, to_node: Any, weight: float = 1.0): ...

    @abstractmethod
    def remove_edge(self, from_node: Any, to_node: Any): ...

    @abstractmethod
    def get_neighbors(self, node_id: Any) -> List[Any]: ...
