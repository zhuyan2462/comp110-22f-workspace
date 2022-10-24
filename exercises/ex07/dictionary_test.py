"""Three list functions written for unit test."""
__author__: str = "731615250"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert_empty() -> None:
    """Test when the dictionary is empty."""
    xs = {}
    assert invert(xs) == {}


def test_invert_one_pair() -> None:
    """Test when the dictionary has one key-value pair."""
    xs = {"Flower": "good"}
    assert invert(xs) == {"good": "Flower"}


def test_invert_many_pairs() -> None:
    """Test when the dictionary has more than one key-value pairs."""
    xs = {"Flower": "good", "Smoke": "bad"}
    assert invert(xs) == {"good": "Flower", "bad": "Smoke"}


def test_favorite_color_empty() -> None:
    """Test when the dictionary is empty."""
    xs = {}
    assert favorite_color(xs) == {}


def test_favorite_color_same_color() -> None:
    """Test when everyone has the same favorite color."""
    xs = {"Eric": "blue", "Lisa": "blue"}
    assert favorite_color(xs) == "Blue"


def test_favorite_color_tie() -> None:
    """Test when there is a tie for the best color."""
    xs = {"Eric": "blue", "Lisa": "yellow"}
    assert favorite_color(xs) == "Blue"


def test_count_empty() -> None:
    """Test when the list is empty."""
    xs = list()
    assert count(xs) == {}


def test_count_one_item() -> None:
    """Test when the list has one item."""
    xs = ["good"]
    assert count(xs) == {"good": 1}


def test_count_many_items() -> None:
    """Test when the list has more than one items."""
    xs = ["good", "good", "bad"]
    assert count(xs) == {"good": 2, "bad": 1}