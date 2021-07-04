"""Making a Simple Dartboard
Create a function which creates a square dartboard of side length n. The value of a number should increase, the closer it is to the centre of the board.

Notes
If the size given is an even number, the centre should be made up of the 4 highest values.
"""


def make_dartboard(size):
    pass


if __name__ == '__main__':
    assert make_dartboard(3) == [
        111,
        121,
        111
    ]
    assert make_dartboard(8) == [
        11111111,
        12222221,
        12333321,
        12344321,
        12344321,
        12333321,
        12222221,
        11111111
    ]
    assert make_dartboard(5) == [
        11111,
        12221,
        12321,
        12221,
        11111
    ]
    print("All cases passed!")
