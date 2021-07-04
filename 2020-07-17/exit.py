"""Can You Exit the Maze?
A maze can be represented by a 2D matrix, where 0s represent walkeable areas, and 1s represent walls. 
You start on the upper left corner and the exit is on the most lower right cell.

Create a function that returns true if you can walk from one end of the maze to the other. 
You can only move up, down, left and right. You cannot move diagonally.

can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
]) -> true

Notes

In a maze of size m x n, you enter at [0, 0] and exit at [m-1, n-1].
There can be dead ends in a maze - one exit path is sufficient.
"""


def can_exit(maze):
    pass


if __name__ == '__main__':
    assert can_exit([
        [0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0]
    ]) == True
    assert can_exit([
        [0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 1]
    ]) == False  # This maze only has dead ends!
    assert can_exit([
        [0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1]
    ]) == False  # Exit only one block away, but unreachable!
    assert can_exit([
        [0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0]
    ]) == True
    print("All cases passed!")
