"""Isolated or Grouped?
Write a function that extracts the max value of a number in a list. If there are
two or more max values, return it as a list, otherwise, return the number. This
process could be relatively easy with some of the built-in list functions but
the required approach is RECURSIVE.
"""


def iso_group(list):
    pass


if __name__ == "__main__":
    assert iso_group([31, 7, 2, 13, 7, 9, 10, 13]) == 31
    assert iso_group([1, 3, 9, 5, 1, 7, 9, -9]) == [9, 9]
    assert iso_group([97, 19, -18, 97, 36, 23, -97]) == [97, 97]
    assert iso_group([-31, -7, -13, -7, -9, -13]) == [-7, -7]
    assert iso_group([-1, -3, -9, -5, -1, -7, -9, -9]) == [-1, -1]
    assert iso_group([107, 19, -18, 79, 36, 23, 97]) == 107
    print("All cases passed!")
