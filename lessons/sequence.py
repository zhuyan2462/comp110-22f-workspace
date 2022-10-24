"""Notes and examples of tup;e and range sequence types."""

# Declaring a types alias that "invent" the Point2D type
# Camel casing - no space between words
from tkinter.font import names


Point2D = tuple[float, float]

start_position: Point2D = (5.0, 10.0)
star_position = (start_position[0] + 5.0, start_position[1] + 10.0)
end_position: Point2D = (99.0, 99.0)

# tuples, because they are a sequence, are 0-indexed

print(start_position)

for item in end_position:
    print(item)

print(len(end_position))

# Exampeles of ranges
a_range: range = range(0, 10, 3)
# Acess its items
print(a_range[0])
print(a_range[1])
print(len(a_range))
for i in a_range:
    print(i)

# An example of using the default parameter step
# Where the defalt step is 1
another_range: range = range(0, 10)

# If you only pass one argument to range, it specifies
# The stop marker ad start is 0 by default
zero_start: range = range(0, 10)
for x in zero_start:
    print(x)

nmes: list[str] = ["Kris", "ALyssa", "Ben", "Arnold"]

for name in names:
    print(name)

# Range is often used to write for loops where you iteration pattern is not consecutive
for i in range(0, len(names), 2):
    print(names[i])