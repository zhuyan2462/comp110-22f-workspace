"""Three list functions written for unit test."""
__author__: str = "731615250"


def only_evens(ints_list: list[int]) -> list[int]:
    """Create a new list that contains the elements of the input that were even."""
    idx: int = 0
    check_list: list[int] = list()
    if len(ints_list) == 0:
        return list()
    else:
        while idx <= len(ints_list) - 1:
            if ints_list[idx] % 2 == 0:
                check_list.append(ints_list[idx])
            idx += 1
    return check_list


def concat(x: list[int], y: list[int]) -> list[int]:
    """Create a new list that contains all elements in the first list and then the second list."""
    idx_x: int = 0
    idx_y: int = 0
    new_list: list[int] = []
    while idx_x <= len(x) - 1:
        new_list.append(x[idx_x])
        idx_x += 1
    while idx_y <= len(y) - 1:
        new_list.append(y[idx_y])
        idx_y += 1
    return new_list


def sub(int_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generate a list that contains elements between the specified start index and the end index - 1."""
    new_list: list[int] = list()
    if start_index <= end_index - 1:
        if int_list == list() or start_index >= len(int_list) - 1:
            return list()
        elif start_index <= 0:
            idx_one: int = 0
            while idx_one <= end_index - 1:
                new_list.append(int_list[idx_one])
                idx_one += 1
        elif end_index > len(int_list) - 1:
            idx_two: int = start_index
            while idx_two <= len(int_list) - 1:
                new_list.append(int_list[idx_two])
                idx_two += 1
        elif start_index >= 0 and end_index <= len(int_list) - 1:
            idx_three: int = start_index
            while idx_three <= end_index - 1:
                if idx_three >= start_index:
                    new_list.append(int_list[idx_three])
                idx_three += 1
        return new_list