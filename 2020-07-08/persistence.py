""" Persistence
The additive persistence of an integer, n, is the number of times you have to replace n with the sum of its digits
until n becomes a single digit integer.

The multiplicative persistence of an integer, n, is the number of times you have to replace n with the product of
its digits until n becomes a single digit integer.

Create two functions that take an integer as an argument and:

Return its additive persistence.
Return its multiplicative persistence.

additive_persistence(1679583) -> 3
1 + 6 + 7 + 9 + 5 + 8 + 3 = 39
3 + 9 = 12
1 + 2 = 3
It takes 3 iterations to reach a single-digit number.

multiplicative_persistence(77) -> 4
7 x 7 = 49
4 x 9 = 36
3 x 6 = 18
1 x 8 = 8
It takes 4 iterations to reach a single-digit number.
"""


def additive_persistence(number):
    pass


def multiplicative_persistence(number):
    pass


if __name__ == '__main__':
    assert additive_persistence(1679583) == 3
    assert additive_persistence(123456) == 2
    assert additive_persistence(6) == 0
    assert multiplicative_persistence(77) == 4
    assert multiplicative_persistence(123456) == 2
    assert multiplicative_persistence(4) == 0
    print("persistence.py complete")
