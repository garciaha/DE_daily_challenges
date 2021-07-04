"""Symmetrical Patterns
Kathleen owns a beautiful rug store. She likes to group the rugs into 4 mutually 
exclusive categories.

imperfect
horizontally symmetric
vertically symmetric
perfect

An imperfect rug is one that is neither horizontally nor vertically symmetric. Here 
is an example of an imperfect rug:

[
  ["a", "a", "a", "a"],
  ["a", "a", "a", "a"],
  ["a", "a", "b", "b"]
]
The following is an horizontally symmetric rug. You could "fold" the rug across a hypothetical
x-axis, and both sides would be identical. A horizontally symmetric rug is not vertically 
symmetric (otherwise this rug would be classified as perfect ).

[
  ["c", "a", "a", "a"],
  ["b", "b", "b", "b"],
  ["c", "a", "a", "a"]
]
The following is a vertically symmetric rug. You could "fold" the rug across a hypothetical 
y-axis, and both sides would be identical. A vertically symmetric is not horizontally symmetric 
(otherwise this rug would be classified as perfect ).

[
  ["a", "b", "a"],
  ["b", "b", "b"],
  ["a", "b", "a"],
  ["a", "b", "a"]
]
Finally, a perfect rug is one that is both vertically and horizontally symmetric. That is, 
folded either length-wise or width-wise will yield two identical pieces.

[
  ["a", "b", "b", "a"],
  ["b", "b", "b", "b"],
  ["a", "b", "b", "a"]
]
Given a rug of m x n dimension, determine whether it is imperfect, horizontally symmetric, 
vertically symmetric or perfect. Rugs are represented using a two-dimensional array.
"""


def classify_rug(rug):
    pass


if __name__ == "__main__":
    assert classify_rug([
        ["a", "a"],
        ["a", "a"]
    ]) == "perfect"
    assert classify_rug([
        ["a", "a", "b"],
        ["a", "a", "a"],
        ["b", "a", "a"]
    ]) == "imperfect"
    assert classify_rug([
        ["b", "a"],
        ["b", "a"]
    ]) == "horizontally symmetric"
    assert classify_rug([
        ["a", "a"],
        ["b", "b"]
    ]) == "vertically symmetric"
    print("All cases passed!")
