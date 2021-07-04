"""Odd Square Patch
Create a function that takes an array of numbers, and returns the size of the
biggest square patch of odd numbers. See examples for a clearer picture.
"""


def odd_square_patch(board):
    pass


if __name__ == "__main__":
    assert odd_square_patch([
        [1, 2, 4, 9],
        [4, 5, 5, 7],
        [3, 6, 1, 7]
    ]) == 2
    #  The 2x2 square at the lower right
    # ([5, 7] on the 2nd row, [1, 7] on the third).

    assert odd_square_patch([[1, 2, 4, 9]]) == 1
    # An array with a single row can only have a square patch of
    # maximum size 1x1 containing a single odd element.

    assert odd_square_patch([[2, 4, 6]]) == 0
    print("All cases passed!")
