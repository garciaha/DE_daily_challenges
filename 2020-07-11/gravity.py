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
    pass


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
