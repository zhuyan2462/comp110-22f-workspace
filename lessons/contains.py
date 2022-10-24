"""An example of a lst utility algoritm."""

# A funciton with two parameters
# needle - what we are searching for
# haystack - what we searching through.
# Return type: boolean



def contains (needle: str, haystack: list[str]) -> bool:
    # Start from first index
    i: int = 0
    # Loop through each index of list
    while i < len(haystack):
        # Thest if equal to needle
        if haystack[i] == needle:
            # Yes! Return True
            return True
        i += 1
    # Return False
    return False