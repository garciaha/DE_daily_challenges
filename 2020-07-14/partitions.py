"""Partitions of a Natural Number
Create a function that determines the number of partitions of a natural number.

A partition of a number n is an unordered sum of one or more numbers which totals n. For example, the partitions of the number 4 are:

1 + 1 + 1 + 1 = 4
1 + 1 + 2 = 4
1 + 3 = 4
2 + 2 = 4
4 = 4

Since partitions are unordered, the sums 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 4 are considered the same partition.

Notes
Remember the trivial partition n = n. Also, we say there is one way to partition zero; namely, 0 = 0.
"""


def partitions(number):
    pass


if __name__ == '__main__':
    assert partitions(4) == 5
    assert partitions(10) == 42
    assert partitions(0) == 1
    assert partitions(1) == 1
    assert partitions(2) == 2
    print("All cases passed!")
