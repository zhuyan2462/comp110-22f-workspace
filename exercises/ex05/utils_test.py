"""The test for utils."""
__author__: str = "731615250"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_only_evens_empty() -> None:
    """Test when the list is empty."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_single_item() -> None:
    """Test when the list contains only one even number."""
    xs: list[int] = [1, 2, 4]
    assert only_evens(xs) == [1]


def test_only_evens_many_items() -> None:
    """Test when the list contains many even numbers."""
    xs: list[int] = [2, 4, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_concat_two_empty_lists() -> None:
    """Test when two lists are empty."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_same_len() -> None:
    """Test when two lists have the same length."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [3, 4, 5]
    assert concat(x, y) == [1, 2, 3, 3, 4, 5]


def test_concat_different_len() -> None:
    """Test when two lists have different lengths."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4]
    assert concat(x, y) == [1, 2, 3, 4]


def test_sub_empty_list() -> None:
    """Test when the list is empty."""
    int_list: list[int] = []
    x: int = 1
    y: int = 2
    assert sub(int_list, x, y) == []


def test_sub_one_index() -> None:
    """Test when the new list only has one index."""
    int_list: list[int] = [1, 2, 3]
    x: int = 1
    y: int = 2
    assert sub(int_list, x, y) == [2]


def test_sub_many_index() -> None:
    """Test when the new list has more than one index."""
    int_list: list[int] = [1, 2, 3, 4]
    x: int = 1
    y: int = 3
    assert sub(int_list, x, y) == [2, 3]