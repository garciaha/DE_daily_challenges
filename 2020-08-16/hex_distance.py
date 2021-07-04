"""Hexagonal Grid: Distance
A hexagonal grid is a commonly used game board design based on hexagonal tiling. In the following grid, 
the two marked locations have a minimum distance of 6 because at least 6 steps are needed to reach the 
second location starting from the first one.

Write a function that takes a hexagonal grid with two marked locations as input and returns their distance.

The input grid will be a list of strings in which each tile is represented with o and the two marked 
locations with x.

Examples
hex_distance([
  "  o o  ",
  " o x o ",
  "  o x  ",
]) -> 1
"""


def hex_distance(grid):
    pass


if __name__ == "__main__":
    assert hex_distance([
        "  o o  ",
        " o x o ",
        "  o x  ",
    ]) == 1
    assert hex_distance([
        "  o o  ",
        " x o o ",
        "  o x  ",
    ]) == 2
    assert hex_distance([
        "   o o o   ",
        "  o o o o  ",
        " o o o o o ",
        "  x o o x  ",
        "   o o o   ",
    ]) == 3
    print("All cases passed!")
