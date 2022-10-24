"""Three list functions written for unit test."""

__author__: str = "731615250"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Invert the key and the value in a dictionary."""
    result: dict[str, str] = {}
    for key in original:
        result_key: str = original[key]
        if result_key in result:
            raise KeyError
        result[result_key] = key
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Generate the favorate colors from the dictionary."""
    color_look_up: dict[str, int] = {}
    max: int = 0
    max_color: str = ""
    for key in colors:
        if colors[key] in color_look_up:
            color_look_up[colors[key]] += 1
        else:
            color_look_up[colors[key]] = 1
    for key in color_look_up:
        if color_look_up[key] > max:
            max = color_look_up[key]
            max_color = key
    return max_color
    

def count(frequency: list[str]) -> dict[str, int]:
    """Count the number of times that a value appeared in the input list."""
    store: dict[str, int] = {}
    for item in frequency:
        if item in store:
            store[item] += 1
        else:
            store[item] = 1
    return store