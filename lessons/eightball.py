"""A simple eight ball program."""

from random import randiant

quesiton: str = input("Ask a yes/no quesiton...")
response: int = randiant(0,3)

if response == 0:
    print("Yes, definitely.")
elif response == 1:
    print("Ask again later.")
elif response == 2:
    print("You betcha.")
else:
    print("My sources say no.")