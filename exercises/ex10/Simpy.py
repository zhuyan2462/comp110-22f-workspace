"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730615250"


class Simpy:
    """A simpler, single dimension implementation of many of the same capabilities of NumPy."""
    values: list[float]

    def __init__(self, x: list[float]):
        """Initialize the values attribute."""
        self.values = x

    def __repr__(self) -> str:
        """Be called when a Simpy object is converted to a str representation."""
        return (f"Simpy({self.values})")
    
    def fill(self, x: float, y: int) -> None:
        """Fill a Simpy's values with a specific number of repeating values."""
        self.values = []
        i: int = 0
        while i < y:
            self.values.append(x)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values."""
        assert step != 0.0
        if start < 0.0 and stop < 0.0 and step < 0.0:
            while start + step >= stop:
                self.values.append(start)
                start += step
        else:
            while start + step <= stop:
                self.values.append(start)
                start += step
    
    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        result_sum: float = 0.0
        for i in self.values:
            result_sum += i
        return result_sum
    
    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Add addition operators."""
        result: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for x in range(len(self.values)):
                result.append(self.values[x] + rhs.values[x])
        else:
            for y in range(len(self.values)):
                result.append(y + rhs)
        return Simpy(result)
    
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Use power operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for x in range(len(self.values)):
                result.values.append(self.values[x] ** rhs.values[x])
        if isinstance(rhs, float):
            for y in range(len(self.values)):
                result.values.append(self.values[y] ** rhs)
        return result

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Check if two items are equal."""
        result: list[bool] = list()
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for x in range(len(self.values)):
                if self.values[x] == rhs.values[x]:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for y in range(len(self.values)):
                if self.values[y] == rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Check inequality."""
        result: list[bool] = list()
        if isinstance(rhs, float):
            for x in range(len(self.values)):
                if self.values[x] > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for y in range(len(self.values)):
                assert len(self.values) == len(rhs.values)
                if self.values[y] > rhs.values[y]:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Use the subscription operator."""
        if isinstance(rhs, int):
            result_1: float = self.values[rhs]
            return result_1
        else:
            result_2: Simpy = Simpy([])
            for i in range(len(rhs)):
                if rhs[i] is True:
                    result_2.values.append(self.values[i])
            return result_2