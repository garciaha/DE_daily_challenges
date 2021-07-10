"""How Many Digits between 1 and N
Imagine you took all the numbers between 0 and n and concatenated them together into a 
long string. How many digits are there between 0 and n? Write a function that can calculate this.

There are 0 digits between 0 and 1, there are 9 digits between 0 and 10 and 
there are 189 digits between 0 and 100.

Examples:

digits(1) -> 0
digits(10) -> 9
digits(100) -> 189

Notes
The numbers are going to be rather big so creating that string won't be practical.
"""

"""
0	1	0	1 - 1 = 0	
0	10	9	1 * (10 - 1)
0 	100	189	(1 * (10 - 1))  + 2 * (100-10) 
0	2020	6969	(9) + (180) + (3*(1000 - 100)) + (4*(2020-1000))
"""
import math

def digits(number):
    result = 0
    for x in range(2, len(str(number)) + 1):
        result += (x - 1) * (math.pow(10, x - 1) - math.pow(10, x - 2))
    result += len(str(number)) * (number - math.pow(10, len(str(number)) - 1))
    return int(result)

if __name__ == '__main__':
    assert digits(1) == 0
    assert digits(10) == 9
    assert digits(100) == 189
    assert digits(2020) == 6969
    print("All cases passed!")
