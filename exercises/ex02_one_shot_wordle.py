"""EX02 - One-Shot Wordle - Loops!"""
__author__: str = "730615250"

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")
boxes: str = ""
cur_idx: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while cur_idx <= 5:
    if len(guess) == 6:
        if guess[cur_idx] == secret[cur_idx]:
            boxes += GREEN_BOX
        else: 
            alt_idx: int = 0
            existence: bool = False
            while existence or alt_idx <= 5:
                if secret[alt_idx] == guess[cur_idx]:
                    existence = True
                else:
                    alt_idx += 1
            
            if existence is True:
                boxes += YELLOW_BOX
            else:
                boxes += WHITE_BOX

        cur_idx += 1
    else:
        guess = input("That was not 6 letters! Try again: ")

print(boxes)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!") 