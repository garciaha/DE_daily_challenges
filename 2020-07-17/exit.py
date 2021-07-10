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

def adj_list(pos, maze):
    a = pos[0]
    b = pos[1]
    return [(a+x, b+y) for x in range(-1, 2) for y in range(-1, 2) if 0 <= a+x and a+x < len(maze) and 0 <= b+y and b+y < len(maze[a+x]) and maze[a+x][b+y] == 0]


def can_exit(maze):
    start = (0, 0)
    end = (len(maze) - 1, len(maze[0]) - 1)
    queue = [start]
    visited = [start]
    while len(queue) > 0:
        current = queue.pop(0)
        adj = adj_list(current, maze)
        for next in adj:
            if next not in visited:
                queue.append(next)
                visited.append(next)
                if next == end: 
                    return True    
    return False


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
