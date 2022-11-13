""""""

from __future__ import annotations
from typing import Union

class StrArray:
    items: list[str]
    def __init__ (self,items:list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        # Your job:
        # 1. Loop through every item in self's item list
        # 2. Concatenate the rhs parameter
        # 3. Append the concatenated string to result's itemlist attribute
        if isinstance(rhs, str):
            for item in self.items:
                item += rhs
                result.items.append(item)
            # or result.item.append(item + rhs)
            return result
        else:
            # 1. Otehrwise, loop through each index of self's item.
            # 2. Concentenate the corresponding value of rhs's items at same index
            # 3. Append the resulting string to result's items list
            for i in range(len(self.items)):
                result.items.append(self.items[i] + rhs.items[i])
            return result

a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")
print(a + b)