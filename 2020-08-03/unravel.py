"""Unravel all the Possibilities

Write a function that takes in a string and returns all possible combinations. Return the final result in alphabetical order.

Examples
unravel("a[b|c]") -> ["ab", "ac"]

Notes
Think of each element in every block (e.g. [a|b|c]) as a fork in the road.
"""


def unravel(string):
    pass


if __name__ == "__main__":
    assert unravel("a[b|c]de[f|g]") == ["abdef", "acdef", "abdeg", "acdeg"]
    assert unravel("a[b]c[d]") == ["abcd"]
    assert unravel("a[b|c|d|e]f") == ["abf", "acf", "adf", "aef"]
    assert unravel("apple [pear|grape]") == ["apple pear", "apple grape"]
    print("All cases passed!")
