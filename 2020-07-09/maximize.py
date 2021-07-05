""" Maximize
Write a function that makes the first number as large as possible by swapping out its digits for digits in the second number.

To illustrate:

max_possible(9328, 456) -> 9658
# 9658 is the largest possible number built from swaps from 456.
# 3 replaced with 6 and 2 replaced with 5.

Each digit in the second number can only be used once.
Zero to all digits in the second number may be used.
"""


def max_possible(num_1, num_2):
    num1_list = [int(x) for x in str(num_1)]
    num2_sort = sorted([int(x) for x in str(num_2)], reverse = True)
    index = 0
    for x in range(len(num1_list)):
       if num2_sort[index] > num1_list[x]:
           num1_list[x] = num2_sort[index]
           index += 1
           if index >= len(num2_sort):
               break
    return int("".join([str(x) for x in num1_list]))
if __name__ == '__main__':
    assert max_possible(523, 76) == 763
    assert max_possible(9132, 5564) == 9655
    assert max_possible(8732, 91255) == 9755
    print("All cases passed!")
