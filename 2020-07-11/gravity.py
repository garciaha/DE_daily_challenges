"""Switch On The Gravity
Given a 2D array of some suspended blocks (represented as hastags), return another 2D
array which shows the end result once gravity is switched on.

switch_gravity_on([
  ["-", "#", "#", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"]
]) -> [
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "#", "#", "-"]
]

Notes
Each block falls individually, meaning there are no rigid objects.
Think about it like falling sand in Minecraft as opposed to the rigid blocks in Tetris.
"""


def switch_gravity_on(number):
    count = [0 for col in range(len(number[0]))]
    for row in range(len(number)):
        for col in range(len(number[row])):
            count[col] += 1 if number[row][col] == "#" else 0
    new_grid = [["-" for x in range(len(number[0]))] for y in range(len(number))]
    for x in range(len(count)):
        for y in range(count[x]):
            new_grid[len(number) - y - 1][x] = "#"
    return new_grid

if __name__ == '__main__':
    assert switch_gravity_on([
        ["-", "#", "#", "-"],
        ["-", "-", "-", "-"],
        ["-", "-", "-", "-"],
        ["-", "-", "-", "-"]
    ]) == [
        ["-", "-", "-", "-"],
        ["-", "-", "-", "-"],
        ["-", "-", "-", "-"],
        ["-", "#", "#", "-"]
    ]
    assert switch_gravity_on([
        ["-", "#", "#", "-"],
        ["-", "-", "#", "-"],
        ["-", "-", "-", "-"],
    ]) == [
        ["-", "-", "-", "-"],
        ["-", "-", "#", "-"],
        ["-", "#", "#", "-"]
    ]
    assert switch_gravity_on([
        ["-", "#", "#", "#", "#", "-"],
        ["#", "-", "-", "#", "#", "-"],
        ["-", "#", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-"]
    ]) == [
        ["-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-"],
        ["-", "#", "-", "#", "#", "-"],
        ["#", "#", "#", "#", "#", "-"]
    ]
    print("All cases passed!")
