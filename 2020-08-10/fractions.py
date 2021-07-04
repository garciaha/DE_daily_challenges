"""Repeating Decimals to Fractions
Performing division on a fraction often results in an infinitely repeating decimal.

1/3=.3333333...  1/7=.142857142857...
Create a function that takes a decimal in string form with the repeating part in parentheses 
and returns the equivalent fraction in string form and in lowest terms.

Examples
fractions("0.(6)") -> "2/3"
fractions("1.(1)") -> "10/9"
"""

"""
This can be done by setting number = x and doing some algebra:

10x = 6.6666....
- x = 0.6666....
--------------
 9x = 6
  x = 6/9 = 2/3

1000000x = 3142857.142857....
-      x =       3.142857....
-------------------------
  99999x = 3142854
       x = 3142854/999999 = 22/7

1000000x = 192367.2367....
-   100x =     19.2367....
------------------------------
 999900x = 192348
       x = 192348/999900 = 5343/27775
"""


def fractions(number):
    pass


if __name__ == "__main__":
    assert fractions("0.(6)") == "2/3"
    assert fractions("1.(1)") == "10/9"
    assert fractions("3.(142857)") == "22/7"
    assert fractions("0.19(2367)") == "5343/27775"
    assert fractions("0.1097(3)") == "823/7500"
    print("All cases passed!")
