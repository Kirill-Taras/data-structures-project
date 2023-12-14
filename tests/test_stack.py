"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack

test_node = Node(1, 2)
test_stack = Stack()


def test_init_node():
    assert test_node.data == 1
    assert test_node.next_node == 2


def test_init_stack():
    assert test_stack.top is None
