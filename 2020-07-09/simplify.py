""" Simplified Fractions
Create a function that returns the simplified version of a fraction.

Example
simplify("4/6") -> "2/3"

A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator. 
For example, 4/6 is not simplified, since 4 and 6 both share 2 as a factor.
If improper fractions can be transformed into integers, do so in your code.

"""


def simplify(fraction):
    frac = fraction.split("/")
    frac = [int(x) for x in frac]
    for i in range(frac[0], 1, -1):
        if frac[0] % i == 0 and frac[1] % i == 0:
            frac[0] = frac[0] / i
            frac[1] = frac[1] / i
    if frac[1] == 1:
        return str(int(frac[0]))
    else:
        return str(int(frac[0])) + "/" + str(int(frac[1]))


if __name__ == '__main__':
    assert simplify("4/6") == "2/3"
    assert simplify("10/11") == "10/11"
    assert simplify("100/400") == "1/4"
    assert simplify("8/4") == "2"
    print("All cases passed!")
