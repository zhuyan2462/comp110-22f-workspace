""""""

from __future__ import annotations
from typing import Union

class StrArray:
    items: list[str]
    def __init__ (self,items:list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: str) -> StrArray:
        result: StrArray = StrArray([])
        # Your job:
        # 1. Loop through every item in self's item list
        # 2. Concatenate the rhs parameter
        # 3. Append the concatenated string to result's itemlist attribute
        for item in self.items:
            item += rhs
            result.items.append(item)
        return result

a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")