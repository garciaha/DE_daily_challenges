"""Josephus Problem
This classic problem dates back to Roman times. There are 41 soldiers arranged in a circle. Every third soldier 
is to be killed by their captors, continuing around the circle until only one soldier remains. He is to be freed. 
Assuming you would like to stay alive, at what position in the circle would you stand?

Generalize this problem by creating a function that accepts the number of soldiers n and the interval at which 
they are killed i, and returns the position of the fortunate survivor.

Examples
josephus(41, 3) -> 31

Notes
Assume the positions are numbered 1 to n going clockwise around the circle.
If the interval is 3, the first soldiers to die are at positions 3, 6, and 9.
"""


def josephus(soldiers, interval):
    pass


if __name__ == '__main__':
    assert josephus(41, 3) == 31
    assert josephus(35, 11) == 18
    assert josephus(11, 1) == 11
    assert josephus(2, 2) == 1
    print("All cases passed!")
