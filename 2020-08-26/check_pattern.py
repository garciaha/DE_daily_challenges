"""Fit the Pattern
Create a function that checks if the sub-arrays in an array adhere to the 
specified pattern.

Notes
- The length of the pattern will always be the same as the length of the (main) 
  array.
- The pattern does not necessarily have to be alphabetically ordered.
"""


def check_pattern(arrays, pattern):
    pass


if __name__ == "__main__":
    assert check_pattern(
        [[1, 1], [2, 2], [1, 1], [2, 2]],
        "ABAB") == True
    assert check_pattern(
        [[1, 2], [1, 3], [1, 4], [1, 2]],
        "ABCA") == True
    assert check_pattern(
        [[1, 2, 3], [1, 2, 3], [3, 2, 1], [3, 2, 1]],
        "AABB") == True
    assert check_pattern(
        [[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]],
        "ABCD") == True
    assert check_pattern(
        [[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]],
        "DCBA") == True
    print("All cases passed!")
