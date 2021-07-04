"""True or False Array?
I admit, this challenge is somehow strange. The objective is to find out if a
given array is true or false. Here are some true arrays:

[12, 40, 4, 6420, 20, 24, 400, 24]
[12.3, 46, 4, 7383, 23, 27, 529, 27.6]
[14, 80, 6, 12840, 40, 46, 1600, 48]

And here some false arrays:

[18.1, 162, 9, 26091, 81, 90, 6561, 97]
[14.5, 90, 18, 14445, 18, 51, 2025, 54]
[19.2, 184, 9, 29592, 92, 101, 8464, 110.8]

All the 8 values in the arrays are connected in some way, you have to find out
what the connection is.

Note:
- Looking at the fifth element of each array will give you a head start
"""


def true_or_false(numbers):
    pass


if __name__ == "__main__":
    assert true_or_false([12, 40, 4, 6420, 20, 24, 400, 24]) == True
    assert true_or_false([18.1, 162, 9, 26091, 81, 90, 6561, 97]) == False
    assert true_or_false([14.7, 94, 6, 15087, 47, 53, 2209, 56.4]) == True
    assert true_or_false([11.5, 30, 3, 4815, 15, 18, 225, 18]) == True
    assert true_or_false([11.5, 30, 3, 4815, 15, 18, 225, 18]) == True
    assert true_or_false([14.5, 90, 6, 14445, 45, 51, 2025, 54]) == True
    assert true_or_false([19, 180, 9, 28890, 90, 99, 8100, 108]) == True
    assert true_or_false([16.5, 130, 8, 20865, 65, 73, 4225, 78]) == True
    assert true_or_false([17.8, 156, 8, 25038, 78, 86, 6084, 93.6]) == True
    assert true_or_false([22.5, 250, 11, 40125, 125, 136, 15625, 150]) == True
    assert true_or_false([12.9, 59, 5, 9309, 29, 34, 841, 44.8]) == False
    assert true_or_false([13.1, 62, 5, 9951, 33, 36, 961, 37.2]) == False
    assert true_or_false([15.4, 108, 7, 17334, 12, 61, 2916, 64.8]) == False
    assert true_or_false([19.8, 196, 9, 31458, 91, 107, 9604, 117.6]) == False
    assert true_or_false([15.1, 102, 7, 16371, 31, 58, 2601, 61.2]) == False
    assert true_or_false([15.9, 118, 7, 18939, 89, 66, 3481, 70.8]) == False
    print("All cases passed!")
