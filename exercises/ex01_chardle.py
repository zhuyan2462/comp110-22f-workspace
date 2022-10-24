"""EX01 -  Chardle - A cute step toward Wordle."""
__author__ = "730615250"

five_characters: str = input("Enter a 5-character word: ")
if len(five_characters) != 5:
    print("Error: Word must contain 5 characters")
    exit()
one_character: str = input("Enter a single character: ")
if len(one_character) != 1:
    print("Error: Character must be a single character")
    exit()
number: int = 0
print("Searching for " + one_character + " in " + five_characters)


if one_character == five_characters[len(five_characters) - 5]:
    print(one_character + " found at index 0")
    number = number + 1
else:
    number = number + 0

if one_character == five_characters[len(five_characters) - 4]:
    print(one_character + " found at index 1")
    number = number + 1
else:
    number = number + 0

if one_character == five_characters[len(five_characters) - 3]:
    print(one_character + " found at index 2")
    number = number + 1
else:
    number = number + 0

if one_character == five_characters[len(five_characters) - 2]:
    print(one_character + " found at index 3")
    number = number + 1
else:
    number = number + 0

if one_character == five_characters[len(five_characters) - 1]:
    print(one_character + " found at index 4")
    number = number + 1
else:
    number = number + 0

if number == 0:  
    print("No instances of " + one_character + " found in " + five_characters)
else:
    if number == 1:
        print(" 1 instance of " + one_character + " found in " + five_characters)
    else:
        print(str(number) + " instances of " + one_character + " found in " + five_characters)