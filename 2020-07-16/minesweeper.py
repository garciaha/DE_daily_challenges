"""Minesweeper I - Grid
This challenge is based on the game Minesweeper.

Create a function that takes a list of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot. 
Return a list where each dash is replaced by a digit indicating the number of mines immediately adjacent to the 
spot (horizontally, vertically, and diagonally).

num_grid([
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) -> [
  ["0", "0", "0", "0", "0"],
  ["0", "1", "1", "1", "0"],
  ["0", "1", "#", "1", "0"],
  ["0", "1", "1", "1", "0"],
  ["0", "0", "0", "0", "0"],
]
"""

def adj_list(pos, board):
    a = pos[0]
    b = pos[1]
    return [(a + x, b + y) for x in range(-1, 2) for y in range(-1, 2) if 0 <= a + x and a + x < len(board) and 0 <= b + y and b + y < len(board[a+x]) and board[a+x][b+y] == "#"]

def num_grid(grid):
    result = grid[:]
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "-":
                result[x][y] = str(len(adj_list((x, y), grid)))
    return result


if __name__ == '__main__':
    assert num_grid([
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]) == [
        ["0", "0", "0", "0", "0"],
        ["0", "1", "1", "1", "0"],
        ["0", "1", "#", "1", "0"],
        ["0", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert num_grid([
        ["-", "-", "-", "-", "#"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["#", "-", "-", "-", "-"]
    ]) == [
        ["0", "0", "0", "1", "#"],
        ["0", "1", "1", "2", "1"],
        ["0", "1", "#", "1", "0"],
        ["1", "2", "1", "1", "0"],
        ["#", "1", "0", "0", "0"]
    ]
    assert num_grid([
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]) == [
        ["1", "1", "2", "#", "#"],
        ["1", "#", "3", "3", "2"],
        ["2", "4", "#", "2", "0"],
        ["1", "#", "#", "2", "0"],
        ["1", "2", "2", "1", "0"],
    ]
    print("All cases passed!")
