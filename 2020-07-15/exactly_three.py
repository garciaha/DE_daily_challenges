"""Exactly Three
You are given a number n. Determine whether n has exactly 3 divisors or not.

Examples
is_exactly_three(4) -> True
# 4 has only 3 divisors: 1, 2 and 4

Notes
"""


def is_exactly_three(number):
    divisors = []
    for x in range(1, number + 1):
        if number % x == 0:
            divisors.append(x)
            if len(divisors) > 3:
                return False
    return len(divisors) == 3

if __name__ == '__main__':
    assert is_exactly_three(4) == True  # 4 has only 3 divisors: 1, 2 and 4
    # 12 has 6 divisors: 1, 2, 3, 4, 6, 12
    assert is_exactly_three(12) == False
    assert is_exactly_three(25) == True  # 25 has only 3 divisors: 1, 5, 25
    print("All cases passed!")
