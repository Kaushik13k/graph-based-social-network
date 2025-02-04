import pytest
from app.custom_graph.edge import Edge


def test_edge_initialization():
    edge = Edge("A", "B", 2.5)
    assert edge.from_node == "A"
    assert edge.to_node == "B"
    assert edge.weight == 2.5


def test_edge_default_weight():
    edge = Edge("A", "B")
    assert edge.weight == 1.0


def test_edge_repr():
    edge = Edge("A", "B", 2.5)
    assert repr(edge) == "Edge(A -> B, weight=2.5)"


def test_edge_equality_same_edges():
    edge1 = Edge("A", "B", 2.5)
    edge2 = Edge("A", "B", 2.5)
    assert edge1 == edge2


def test_edge_inequality_different_weights():
    edge1 = Edge("A", "B", 2.5)
    edge2 = Edge("A", "B", 1.0)
    assert edge1 != edge2


def test_edge_hashing():
    edge1 = Edge("A", "B", 2.5)
    edge2 = Edge("A", "B", 2.5)
    edge_set = {edge1}
    assert edge2 in edge_set
