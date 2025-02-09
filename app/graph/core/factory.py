from core.graph import Graph


class GraphFactory:
    @staticmethod
    def create_graph(directed: bool = False) -> Graph:
        return Graph(directed)
