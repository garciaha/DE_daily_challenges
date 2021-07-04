"""Build a Diamond Machine
You are a skilled diamondsmith whose business is getting better by the day. Eventually, you decided that 
you needed to scale to keep up with demand.

- Build a diamond-cutting machine (i.e. write a function that takes in a positive integer representing the 
  raw stone's carat).
- The output would be the finished diamond and tag indicating its quality, arranged in a list or array of 
  two elements.
- The first element would be a list of lists or array of arrays representing the diamond
- The second element would be a string indicating 'perfect cut' if all the diamond's edges are pointy or 
  'good cut' otherwise.

Examples

diamond(3) -> [
  [[0, 1, 0],
   [1, 0, 1],
   [0, 1, 0]],
  "perfect cut"
]
# Perfect edge.

diamond(4) -> [
  [[0, 1, 1, 0],
   [1, 0, 0, 1],
   [0, 1, 1, 0]],
  "good cut"
]
# First and last rows had blunt edges with two 1s each.

Notes
- Cut is more important than carat in the diamondsmith's world. Hence, to reduce the number of blunt edges, 
  the machine would reduce the size of the diamond.
- In the second example of a 4-carat raw stone, the machine produces a finished diamond of only 3 rows so that 
  there would only be 2 blunt edges, instead of 4.
- In the first and third examples, the machine was able to produce diamonds of n-rows from n-carat stones.
"""


def diamond(carats):
    pass


if __name__ == "__main__":
    assert diamond(3) == [
        [[0, 1, 0],
         [1, 0, 1],
         [0, 1, 0]],
        "perfect cut"
    ]  # Perfect edge.
    assert diamond(4) == [
        [[0, 1, 1, 0],
         [1, 0, 0, 1],
         [0, 1, 1, 0]],
        "good cut"
    ]  # First and last rows had blunt edges with two 1s each.
    assert diamond(11) == [
        [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]],
        "perfect cut"
    ]
    print("All cases passed!")
