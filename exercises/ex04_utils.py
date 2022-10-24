"""Three list utility functions."""
__author__: str = "731615250"

 
def all(number_list: list[int], target: int) -> bool:
    """Check if one integers can be found in the list."""
    idx: int = 0
    if len(number_list) == 0:
        return False
    while idx <= len(number_list) - 1:
        if number_list[idx] != target:
            return False
        else:
            idx += 1
    return True


def max(number_list: list[int]) -> int:
    """Find the maximun number in the list."""
    idx: int = 1
    max_number: int = number_list[0]
    if len(number_list) == 0:
        raise ValueError("max() arg is an empty list")
    while idx <= len(number_list) - 1:
        if number_list[idx] > max_number:
            max_number = number_list[idx]
        idx += 1
    return max_number


def is_equal(input_one: list[int], input_two: list[int]) -> bool:
    """Check if two lists are equal."""
    idx: int = 0
    if len(input_one) != len(input_two):
        return False
    while idx <= len(input_one) - 1:
        if input_one[idx] == input_two[idx]:
            idx += 1
        else:
            return False
    return True        