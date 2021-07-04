"""Chain Reaction (Part 1)
In this challenge you will be given a rectangular list representing a "map" with
three types of spaces:

- "+" bombs: When activated, their explosion activates any bombs directly above,
  below, left, or right of the "+" bomb.
- "x" bombs: When activated, their explosion activates any bombs placed in any 
  of the four diagonal directions next to the "x" bomb.
- Empty spaces "0".

Consider the grid:

[
  ["+", "+", "0", "x", "x", "+", "0"],
  ["0", "+", "+", "x", "0", "+", "x"]
]

If the top left "+" bomb explodes, the resulting chain reaction will blow up
bombs in the order given by the numbers below:

[
  ["1", "2", "0", "x", "6", "8", "0"],
  ["0", "3", "4", "5", "0", "7", "8"]
]

Note that there are two 8's since two of the bombs explode at the same time.
Also, note that one of the "x" bombs in the top row does not explode.

Write a function that determines if the chain reaction started when the top left
bomb explodes destroys all bombs or not.

Notes
Both "+" and "x" bombs have an "explosion range" of 1.
"""


def all_explode(bombs):
    pass


if __name__ == "__main__":
    assert all_explode([
        ["+", "+", "+", "+", "+", "+", "x"]
    ]) == True
    assert all_explode([
        ["+", "+", "+", "+", "+", "0", "x"]
    ]) == False
    assert all_explode([
        ["+", "+", "0", "x", "x", "+", "0"],
        ["0", "+", "+", "x", "0", "+", "x"]
    ]) == False
    assert all_explode([
        ["x", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "x"]
    ]) == False
    assert all_explode([
        ["x", "0", "x"],
        ["0", "x", "0"],
        ["x", "0", "x"]
    ]) == True
    print("All cases passed!")
