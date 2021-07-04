"""Bingo Check
Create a function that takes a 5x5 3D list and returns True if it has at least
one Bingo, and False if it doesn't.

Notes
Only check for diagnols, horizontals and verticals.
"""


def bingo_check(board):
    pass


if __name__ == "__main__":
    assert bingo_check([
        [45, "x", 31, 74, 87],
        [64, "x", 47, 32, 90],
        [37, "x", 68, 83, 54],
        [67, "x", 98, 39, 44],
        [21, "x", 24, 30, 52]
    ]) == True
    assert bingo_check([
        ["x", 43, 31, 74, 87],
        [64, "x", 47, 32, 90],
        [37, 65, "x", 83, 54],
        [67, 98, 39, "x", 44],
        [21, 59, 24, 30, "x"]
    ]) == True
    assert bingo_check([
        ["x", "x", "x", "x", "x"],
        [64, 12, 47, 32, 90],
        [37, 16, 68, 83, 54],
        [67, 19, 98, 39, 44],
        [21, 75, 24, 30, 52]
    ]) == True
    assert bingo_check([
        [45, "x", 31, 74, 87],
        [64, 78, 47, "x", 90],
        [37, "x", 68, 83, 54],
        [67, "x", 98, "x", 44],
        [21, "x", 24, 30, 52]
    ]) == False
    print("All cases passed!")
