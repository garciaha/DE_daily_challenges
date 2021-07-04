"""Frequency by Level of Nesting
Create a function that takes in a nested list and an element and returns the 
frequency of that element by nested level.

Examples
freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1) -> [[0, 1], [1, 2], [2, 3]]
# The list has one 1 at level 0, 2 1's at level 1, and 3 1's at level 2.

Notes
- Start the default nesting (a list with no nesting) at 0.
- Output the nested levels in order (e.g. 0 first, then 1, then 2, etc).
- Output 0 for the frequency if that particular level has no instances of that 
  element.
"""


def freq_count(arrays, num):
    pass


if __name__ == "__main__":
    assert freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1) == [
        [0, 1], [1, 2], [2, 3]]
    # The list has one 1 at level 0, 2 1's at level 1, and 3 1's at level 2.
    assert freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5) == [
        [0, 3], [1, 4], [2, 0]]
    assert freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2) == [
        [0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]
    print("All cases passed!")
