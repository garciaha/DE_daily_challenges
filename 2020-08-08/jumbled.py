"""Jumbled Equations
In this challenge, you are given a list of one or more arithmetic operators and a 
list of numbers. Take each of the operators and mate it with any three separate 
numbers in the list to create a valid equation. Your answer should contain all 
possible equations.

Examples
jumbled([["+"], [2, 1, 3]]) -> ["1+2=3"]

Notes
For operators with commutative properties, return only the equation with the 
smallest term first. "4*6=24" not "6*4=24".

Return your answer as a list sorted lexicographically.
"""


def jumbled(equation):
    pass


if __name__ == "__main__":
    assert jumbled([["+"], [2, 1, 3]]) == ["1+2=3"]
    assert jumbled([["+", "*"], [36, 28, 71, 4, 12, 7, 11]]
                   ) == ["4*7=28", "4+7=11"]
    assert jumbled([["+", "-", "*", "**"], [1, 2, 3, 0]]
                   ) == ["1+2=3", "2**0=1", "3**0=1", "3-1=2", "3-2=1"]
    # Each equation must contain 3 discrete numbers from the list.
    # "1+0=1" or "3-3=0" are not allowed.
    print("All cases passed!")
