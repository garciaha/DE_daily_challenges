"""Outward Counterclockwise Spiral Matrix Traversal
Write a function that accepts four arguments. The first two arguments are the
size of the grid (h x w), filled with ascending integers from left to right,
top to bottom, starting from 1. The next two arguments are is the starting
positions, the row (r) and column (c).

Return an array of integers obtained by spiraling outward anti-clockwise from
the r and c, starting upward.

    Returns an array of integers obtained by spiralling outward anti-clockwise
    from the r and c, starting upward.
    Args:
        h (int): The layout height.
        w (int): The layout width.
        r (int): The starting row.
        c (int): The starting column.
    Returns:
        list. The spiral representation.
    Raises:
        ValueError
"""


def outward_spiral(h, w, r, c):
    pass


if __name__ == "__main__":
    assert outward_spiral(0, 0, 0, 0) == "Invalid layout size"
    assert outward_spiral(1, 1, 0, 0) == "Invalid starting point"
    assert outward_spiral(1, 1, 2, 1) == "Invalid starting point"
    assert outward_spiral(1, 1, 1, 1) == [1]
    assert outward_spiral(2, 1, 2, 1) == [2, 1]
    assert outward_spiral(2, 1, 1, 1) == [1, 2]
    assert outward_spiral(2, 2, 2, 2) == [4, 2, 1, 3]
    assert outward_spiral(2, 2, 1, 2) == [2, 1, 3, 4]
    assert outward_spiral(2, 2, 1, 1) == [1, 3, 4, 2]
    assert outward_spiral(2, 4, 1, 2) == [2, 1, 5, 6, 7, 3, 8, 4]
    assert outward_spiral(5, 5, 3, 3) == [
        13, 8, 7, 12, 17, 18, 19, 14, 9, 4, 3, 2, 1, 6, 11,
        16, 21, 22, 23, 24, 25, 20, 15, 10, 5]
    print("All cases passed!")
