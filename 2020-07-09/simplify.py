""" Simplified Fractions
Create a function that returns the simplified version of a fraction.

Example
simplify("4/6") -> "2/3"

A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator. 
For example, 4/6 is not simplified, since 4 and 6 both share 2 as a factor.
If improper fractions can be transformed into integers, do so in your code.

"""


def simplify(fraction):
    pass


if __name__ == '__main__':
    assert simplify("4/6") == "2/3"
    assert simplify("10/11") == "10/11"
    assert simplify("100/400") == "1/4"
    assert simplify("8/4") == "2"
    print("All cases passed!")
