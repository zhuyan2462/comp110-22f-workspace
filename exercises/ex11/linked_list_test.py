"""Tests for linked list utils."""

import pytest 
from exercises.ex11.linked_list import Node, last

__author__ = "730615250"

def test_last_empty() -> None:
    """Last of an empty Linked list should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)
    
def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3