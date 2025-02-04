import pytest
from app.custom_graph.graph import Graph
from app.custom_graph.exceptions import NodeNotFoundError, EdgeAlreadyExistsError, NodeAlreadyExistsError


@pytest.fixture
def directed_graph():
    return Graph(directed=True)


def test_add_node(directed_graph):
    directed_graph.add_node("A")
    assert "A" in directed_graph.nodes


def test_add_edge(directed_graph):
    directed_graph.add_node("A")
    directed_graph.add_node("B")
    directed_graph.add_edge("A", "B")
    neighbors = directed_graph.get_neighbors("A")
    assert "B" in neighbors


def test_missing_node_exception(directed_graph):
    with pytest.raises(NodeNotFoundError):
        directed_graph.add_edge("X", "Y")


def test_duplicate_edge_error(directed_graph):
    directed_graph.add_node("A")
    directed_graph.add_node("B")
    directed_graph.add_edge("A", "B")
    with pytest.raises(EdgeAlreadyExistsError):
        directed_graph.add_edge("A", "B")


def test_duplicate_node_error(directed_graph):
    directed_graph.add_node("A")
    with pytest.raises(NodeAlreadyExistsError):
        directed_graph.add_node("A")
