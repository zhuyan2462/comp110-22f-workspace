"""Dictionary related utility functions."""

__author__ = "730615250"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(column: list[dict[str, str]], name: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in column:
        item: str = row[name]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a dictionary that contains several head items in the previous dictionary."""
    result: dict[str, list[str]] = {}
    if n > len(table):
        n = len(table)
    for key in table:
        store: list[str] = []
        i = 0
        while i < n:
            store.append(table[key][i])
            i += 1
        result[key] = store
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for key in names:
        result[key] = table[key]
    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new-column based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in a:
        result[key] = a[key]
    for key in b:
        if key in result:
            for item in b[key]:
                result[key].append(item)
        else:
            result[key] = b[key]
    return result


def count(frequency: list[str]) -> dict[str, int]:
    """Produce a dictionary where each key is a unique value in the given list."""
    result: dict[str, int] = {}
    for item in frequency:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result