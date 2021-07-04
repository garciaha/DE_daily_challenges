"""Trace the Path of the Word
A grid of letters may contain a word hidden somewhere within it.
The letters of the word may be traced from the starting letter by moving a single letter at a
time, up, down, left or right. For example, suppose we are looking
for the word BISCUIT in this grid:

[
  ["B","I","T","R"],
  ["I","U","A","S"],
  ["S","C","V","W"],
  ["D","O","N","E"]
]
The word starts in the top left corner, continues downwards for 2 more letters, then
the letter to the right followed by 2 letters moving upwards, the final letter at the
right of the penultimate one.

Write a function which takes in a target word and a grid of letters and returns a list of
tuples, each tuple being the row and column of the corresponding letter in the grid
(numbered from 0). If the word cannot be found, output the string "Not present".

Notes
The target word will never be longer than the grid of letters.
Target word and the letters grid will be in upper case.
"""


def trace_word_path(word, board):
    pass


if __name__ == '__main__':
    assert str(trace_word_path("BISCUIT", [
        ["B", "I", "T", "R"],
        ["I", "U", "A", "S"],
        ["S", "C", "V", "W"],
        ["D", "O", "N", "E"]
    ])) == str([(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2)])
    assert str(trace_word_path("HELPFUL", [
        ["L", "I", "T", "R"],
        ["U", "U", "A", "S"],
        ["L", "U", "P", "O"],
        ["E", "F", "E", "H"]
    ])) == "Not present"
    assert str(trace_word_path("LUPITA", [
        ["L", "I", "T", "R"],
        ["U", "P", "A", "S"],
        ["P", "U", "P", "O"],
        ["E", "F", "E", "H"]
    ])) == str([(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2)])
    print("All cases passed!")
