"""Coin Trouble
Given a list of coins, father needs to distribute them amongst his three
children. Write a function to determine if the coins can be distributed equally
or not. Return True if each son receives the same amount of money, otherwise
return False.

[1, 2, 3, 2, 2, 2, 3] -> True
Amount to be distributed to each child = (1+2+3+2+4+3)/3 => 15/3 => 5
Possible set of coin to be distributed to children = [(1,2,2),(2,3),(2,3)]

[5, 3, 10, 1, 2] -> False
Amount to be distributed to each child = (5+3+10+1+2)/3 => 21/3 => 7
But there are no combination such that each child get equal value which is 7.

Notes
- Inputs will be an array of positive integers only.
- Coin can be any positive value.
"""


def coins_div(coins):
    pass


if __name__ == "__main__":
    assert coins_div([1, 2, 3, 2, 2, 2, 3]) == True
    assert coins_div([5, 3, 10, 1, 2]) == False
    assert coins_div([2, 4, 3, 2, 4, 9, 7, 8, 6, 9]) == True
    print("All cases passed!")
