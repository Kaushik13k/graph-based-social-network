import pytest
from app.custom_graph.node import Node


def test_node_initialization():
    node = Node(1)
    assert node.node_id == 1


def test_node_repr():
    node = Node("A")
    assert repr(node) == "Node(A)"


def test_node_equality_same_node_id():
    node1 = Node("A")
    node2 = Node("A")
    assert node1 == node2


def test_node_inequality_different_node_id():
    node1 = Node("A")
    node2 = Node("B")
    assert node1 != node2


def test_node_hashing():
    node1 = Node(1)
    node2 = Node(1)
    node_set = {node1}
    assert node2 in node_set
