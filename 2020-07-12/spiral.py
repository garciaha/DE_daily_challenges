"""Spiral Transposition
Create a function that takes a two-dimensional list as an argument and returns a one-dimensional 
list with the values of the original 2d list that are arranged by spiralling through it (starting from the top-left).

spiral_transposition([
  [7, 2],
  [5, 0]
]) -> [7, 2, 0, 5]


Notes
If you do not understand the instructions, write the 3x3 list example on a piece of paper and trace the output through it.
"""


def spiral_transposition(number_lists):
    unspiral = []
    while len(number_lists) > 0:
        # right
        for i in range(len(number_lists[0])):
            unspiral.append(number_lists[0].pop(0))
            if number_lists[0] == []:
                number_lists.pop(0)
        # down
        for i in range(len(number_lists)):
            unspiral.append(number_lists[i].pop(-1))
        if len(number_lists) == 0:
            break
        # left
        for i in range(len(number_lists[-1])):
            unspiral.append(number_lists[-1].pop(-1))
            if number_lists[-1] == []:
                number_lists.pop(-1)
        # up
        for i in range(len(number_lists) - 1, -1, -1):
            unspiral.append(number_lists[i].pop(0)) 
    return unspiral

if __name__ == '__main__':
    assert spiral_transposition([
        [7, 2],
        [5, 0]
    ]) == [7, 2, 0, 5]
    assert spiral_transposition([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_transposition([
        [1, 1, 1],
        [4, 5, 2],
        [3, 3, 2]
    ]) == [1, 1, 1, 2, 2, 3, 3, 4, 5]
    assert spiral_transposition([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    print("All cases passed!")
