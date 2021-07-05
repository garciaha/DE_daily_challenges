"""Ascending Consecutive Numbers
Write a function that returns True if a string consists of ascending AND consecutive numbers.

ascending("232425") -> True
# Consecutive numbers 23, 24, 25

A number can consist of any number of digits, so long as the numbers are adjacent to each other, 
and the string has at least two of them.
"""


def ascending(number):
    lengths = [x for x in range(1, len(number)) if len(number) % x == 0]
    for l in lengths:
        splits = [int(number[(i*l):(i+1)*l]) for i in range(int(len(number) / l))]
        check = [False for i in range(len(splits) - 1) if splits[i] + 1 != splits[i+1]]
        if check == []:
            return True
    return False

if __name__ == '__main__':
    assert ascending("232425") == True  # Consecutive numbers 23, 24, 25
    # No matter how this string is divided, the numbers are not consecutive.
    assert ascending("2324256") == False
    assert ascending("444445") == True  # Consecutive numbers 444 and 445.
    print("All cases passed!")
