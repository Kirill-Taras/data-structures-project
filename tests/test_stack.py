"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack

test_node = Node(1, 2)
test_stack = Stack()


def test_init_node():
    assert test_node.data == 1
    assert test_node.next_node == 2


def test_init_stack():
    assert test_stack.top is None


def test_push_stack(data):
    data.push("123")
    data.push("456")
    data.push("789")
    assert data.top == "789"
    assert data.top.next_node == "456"


def test_pop_stack(data):
    data.push("123")
    data.push("456")
    data.push("789")
    data_1 = data.pop()
    assert data_1 == "789"
    assert data.top == "456"
    assert data.top.next_node == "123"
