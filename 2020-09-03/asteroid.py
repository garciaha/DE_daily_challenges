"""Asteroid Collision
You are given a list asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet,
the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

Notes:
- BONUS: Use only one loop (either for or while).
"""


def asteroid(asteroids):
    pass


if __name__ == "__main__":
    assert asteroid([-2, -1, 1, 2]) == [-2, -1, 1, 2]
    assert asteroid([-2, 1, 1, -2]) == [-2, -2]
    assert asteroid([1, 1, -2, -2]) == [-2, -2]
    assert asteroid([10, 2, -5]) == [10]
    assert asteroid([8, -8]) == []
    print("All cases passed!")
