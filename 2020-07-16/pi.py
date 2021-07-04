"""First n Digits of Pi
As far as we currently know, approximations for the mathematical constant pi in the history of mathematics started surfacing 
with Ancient Babylonians, who found its correct truncation up to 1 decimal place. During the 5th century, the Chinese mathematician 
Zu Chongzhi raised it to 7 decimal places and from the 18th century onwards the number of correct pi decimal places has seen steady growth.

Since the middle of the 20th century, the approximation of pi has been the task of electronic digital computers. During the 2019 
Pi Day on the 14th of March, the Japanese computer scientist Emma Haruka Iwao released the currently most accurate 
value of pi with more than 31.4 trillion digits, using 170 Terabytes of data.

Your task is to create a function that takes a positive integer n as an argument and returns the value of pi with its first 
n decimal digits.

Taylor series are usually used to get finer approximations. To make this challenge approachable to anyone, 
the following formula is suggested:

** See pi_calculation.svg **

Examples
pi(1) -> "3.1"
pi(2) -> "3.14"
pi(10) -> "3.141592653589793238462643383279"
"""
"""
n = 0	i = 0 	3
n = 1	i

3 / 4(3) 1 /4

"""




import math
def pi(decimals):
    pass


if __name__ == '__main__':
    assert pi(1) == "3.1"
    assert pi(2) == "3.14"
    assert pi(10) == "3.1415926535"
    # overflows at 30
    # assert pi(30) == "3.141592653589793238462643383279"
    print("All cases passed!")
