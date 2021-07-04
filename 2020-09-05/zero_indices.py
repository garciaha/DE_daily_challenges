"""Indices of Zeroes for the Longest Run of Contiguous Ones
You are given an array of binary integers and k, the number of flips allowed.

Write a function that returns the indices of zeroes of which, when flipped,
return the longest contiguous sequence of ones.

Notes
If multiple combinations of indices tie for longest one sequence, return the
indices which occur first.
"""


def zero_indices(values, flips):
    pass


if __name__ == "__main__":
    assert zero_indices([1, 0, 1, 1, 0, 0, 0, 1], 1) == [1]
    assert zero_indices([1, 0, 0, 0, 0, 1], 1) == [1]
    assert zero_indices([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 3) == [6, 7, 9]
    assert zero_indices([1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], 3) == [7, 8, 9]
    print("All cases passed!")
