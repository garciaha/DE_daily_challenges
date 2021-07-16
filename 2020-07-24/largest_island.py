"""
Largest Island
An island is a region of contiguous ones. A contiguous one is a 1 that is touched by at least one other 1, either horizontally, vertically or diagonally. Given a piece of the map, represented by a 2-D array, create a function that returns the area of the largest island.

To illustrate, if we were given the following piece of the map, we should return 4.

[
  [0, 0, 0],
  [0, 1, 1],
  [0, 1, 1]
]
Our function should yield 2 for the map below:

[
  [1, 0, 0],
  [0, 0, 1],
  [0, 0, 1]
]
Our function should yield 4 for the map below: :

[
  [1, 0, 0],
  [0, 1, 1],
  [0, 0, 1]
]

Notes
Maps can be any m x n dimension.
Maps will always have at least 1 element. m >= 1 and n >= 1.
"""

def adj_list(pos, m, n, ones):
    a = pos[0]
    b = pos[1] 
    return [(a + x, b + y) for x in range(-1, 2) for y in range(-1, 2) if 0<=a+x and a+x<m and 0<=b+y and b+y<n and (a+x, b+y) in ones]

def largest_island(map):
    ones = [(a, b) for a in range(len(map)) for b in range(len(map[a])) if map[a][b] == 1]
    islands = [len(adj_list(x, len(map), len(map[0]), ones)) for x in ones]
    return max(islands)


if __name__ == '__main__':
    assert largest_island([
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]) == 1
    assert largest_island([
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 1]
    ]) == 5
    assert largest_island([
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 1]
    ]) == 3
    print("All cases passed!")
