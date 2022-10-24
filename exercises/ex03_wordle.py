"""EX03 - Structured Wordle - finally!"""
__author__: str = "731615250"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    counter: int = 1
    secret_word: str = "codes"
    Won: bool = False
    while not Won and counter <= len(secret_word) + 1:
        print(f"=== Turn {counter}/6 ===")
        guess_word: str = input_guess(len(secret_word))
        print(emojified(guess_word, secret_word))
        if guess_word == secret_word:
            Won = True
        else:
            counter += 1
    if Won is True:
        print(f"You won in {counter}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(characters: str, target: str) -> bool:
    """Find target in characters by searching the indexes of characters."""
    assert len(target) == 1
    idx: int = 0
    while idx <= len(characters) - 1:
        if characters[idx] == target[0]:
            return True
        else:
            idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Print emoji boxes to show the result of checking each index of the guess word in the secret word."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    guess_idx: int = 0
    boxes: str = ""
    while guess_idx <= len(guess) - 1:
        if guess[guess_idx] == secret[guess_idx]:
            boxes += GREEN_BOX
        elif contains_char(secret, guess[guess_idx]) is True:
            boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX
        guess_idx += 1
    return boxes


def input_guess(length: int) -> str:
    """Enter a word with specific length."""
    guess_word: str = input(f"Enter a {length} character word: ")
    while len(guess_word) != length:
        guess_word = input(f"That wasn't {length} chars! Try again: ")
    return guess_word


if __name__ == "__main__":
    main()       