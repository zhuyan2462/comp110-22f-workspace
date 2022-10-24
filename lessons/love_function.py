"""SOme tneder, loving function."""
from curses import KEY_RESIZE


def love(subject: str) -> str:
    """Given a subject as a parameter, reutrns a loving string."""
    return f"I love you {subject}!"


def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a lovinv message n times."""
    love_note: str = ""
    number: int= 0
    while number < n:
        #TODO: the real work
        love_note += love(to) + "\n"
        number += 1
    return love_note

