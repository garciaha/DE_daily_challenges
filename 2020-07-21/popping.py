"""Popping Blocks
When two blocks of the same "type" are adjacent to each other, the entire contiguous 
block disappears (pops off). If this occurs, this can allow previously separated blocks 
to be in contact with each other, setting off a chain reaction. This will continue until 
each block is surrounded by a different block.

Here's a demonstration:

["A", "B", "C", "C", "B", "D", "A"]
# The two adjacent Cs pop off

["A", "B", "B", "D", "A"]
# Two adjacent Bs pop off

["A", "D", "A"]
# No more blocks can be popped off

Another demonstration:

["A", "B", "A", "A", "A", "B", "B"]
# The three adjacent As will pop off
# (before the two adjacent Bs)

["A", "B", "B", "B"]
# 3 adjacent Bs pop off

["A"]
# Final result

Notes
If the first round has multiple poppable blocks, pop starting from the left.
"""


def popping(board):
    popped = True
    while popped:
        popped = False
        for x in range(len(board) - 1):
            start = x
            end = x
            while end + 1 < len(board) and board[start] == board[end + 1]:
                end += 1
            if start != end:
                board = board[:start] + board[end+1:]
                popped = True
    return board
if __name__ == '__main__':
    assert popping(["B", "B", "A", "C", "A", "A", "C"]) == ["A"]
    assert popping(["B", "B", "C", "C", "A", "A", "A"]) == []
    assert popping(["C", "A", "C"]) == ["C", "A", "C"]
    assert popping(["Z", "E", "D", "C", "B", "A", "A",
                    "A", "B", "C", "D", "E"]) == ["Z"]
    print("All cases passed!")
