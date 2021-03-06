"""The Jumping Frogs
Three frogs are happily hopping along a narrow board together when they meet another 
group of three frogs traveling in the opposite direction. These frogs can only move in the 
direction they are facing, and only if there is a space directly in front of them. 

Additionally, a frog can jump over the frog in front but only if there is clear space 
on the other side to land in.

Example:

jumping_frogs([1, 1, 0, -1, -1]) ->
    [[1, 1, 0, -1, -1], 
    [1, 0, 1, -1, -1], 
    [1, -1, 1, 0, -1], 
    [1, -1, 1, -1, 0], 
    [1, -1, 0, -1, 1], 
    [0, -1, 1, -1, 1], 
    [-1, 0, 1, -1, 1], 
    [-1, -1, 1, 0, 1], 
    [-1, -1, 0, 1, 1]]

How can the frogs (moving one at a time) pass each other and continue on their way?
"""


def jumping_frogs(board):
    pass


if __name__ == "__main__":
    assert jumping_frogs([1, 1, 0, -1, -1]) == \
        [[1, 1, 0, -1, -1],
         [1, 0, 1, -1, -1],
         [1, -1, 1, 0, -1],
         [1, -1, 1, -1, 0],
         [1, -1, 0, -1, 1],
         [0, -1, 1, -1, 1],
         [-1, 0, 1, -1, 1],
         [-1, -1, 1, 0, 1],
         [-1, -1, 0, 1, 1]]
    assert jumping_frogs([1, 1, 1, 0, -1, -1, -1]) == \
        [[1, 1, 1, 0, -1, -1, -1],
         [1, 1, 0, 1, -1, -1, -1],
         [1, 1, -1, 1, 0, -1, -1],
         [1, 1, -1, 1, -1, 0, -1],
         [1, 1, -1, 0, -1, 1, -1],
         [1, 0, -1, 1, -1, 1, -1],
         [0, 1, -1, 1, -1, 1, -1],
         [-1, 1, 0, 1, -1, 1, -1],
         [-1, 1, -1, 1, 0, 1, -1],
         [-1, 1, -1, 1, -1, 1, 0],
         [-1, 1, -1, 1, -1, 0, 1],
         [-1, 1, -1, 0, -1, 1, 1],
         [-1, 0, -1, 1, -1, 1, 1],
         [-1, -1, 0, 1, -1, 1, 1],
         [-1, -1, -1, 1, 0, 1, 1],
         [-1, -1, -1, 0, 1, 1, 1]]
    assert jumping_frogs([1, 1, 1, 1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1]) == \
        [[1, 1, 1, 1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, 1, 1, 0, 1, -1, -1, -1, -1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, 1, 1, -1, 1, 0, -1, -1, -1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 0, -1, -1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, 1, 1, -1, 0, -1, 1, -1, -1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, 1, 0, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, 0, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, -1, 1, 0, 1, -1, 1, -1, -1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, -1, 1, -1, 1, 0, 1, -1, -1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 0, -1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 0, -1, 1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, -1, 1, -1, 0, -1, 1, -1, 1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1],
         [1, 1, 1, 1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1],
         [1, 1, 1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1],
         [1, 1, 1, -1, 1, 0, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1],
         [1, 1, 1, -1, 1, -1, 1, 0, 1, -1, 1, -1, 1, -1, -1, -1, -1],
         [1, 1, 1, -1, 1, -1, 1, -1, 1, 0, 1, -1, 1, -1, -1, -1, -1],
         [1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0, 1, -1, -1, -1, -1],
         [1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0, -1, -1, -1],
         [1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1, -1],
         [1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1, 1, -1, -1],
         [1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1, 1, -1, 1, -1, -1],
         [1, 1, 1, -1, 1, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, -1],
         [1, 1, 1, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1],
         [1, 1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1],
         [1, 1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1],
         [1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1],
         [1, -1, 1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1],
         [1, -1, 1, -1, 1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1],
         [1, -1, 1, -1, 1, -1, 1, 0, 1, -1, 1, -1, 1, -1, 1, -1, -1],
         [1, -1, 1, -1, 1, -1, 1, -1, 1, 0, 1, -1, 1, -1, 1, -1, -1],
         [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0, 1, -1, 1, -1, -1],
         [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0, 1, -1, -1],
         [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0, -1],
         [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0],
         [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1, 1],
         [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1, 1, -1, 1],
         [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1],
         [1, -1, 1, -1, 1, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1],
         [1, -1, 1, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
         [1, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
         [1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
         [0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
         [-1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
         [-1, -1, 1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
         [-1, -1, 1, -1, 1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
         [-1, -1, 1, -1, 1, -1, 1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1],
         [-1, -1, 1, -1, 1, -1, 1, -1, 1, 0, 1, -1, 1, -1, 1, -1, 1],
         [-1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0, 1, -1, 1, -1, 1],
         [-1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0, 1, -1, 1],
         [-1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0, 1],
         [-1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 1, 1],
         [-1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1, 1, 1, 1],
         [-1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1, 1, -1, 1, 1, 1],
         [-1, -1, 1, -1, 1, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, 1, 1],
         [-1, -1, 1, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1],
         [-1, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1],
         [-1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1],
         [-1, -1, -1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1],
         [-1, -1, -1, -1, 1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1],
         [-1, -1, -1, -1, 1, -1, 1, 0, 1, -1, 1, -1, 1, -1, 1, 1, 1],
         [-1, -1, -1, -1, 1, -1, 1, -1, 1, 0, 1, -1, 1, -1, 1, 1, 1],
         [-1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 0, 1, -1, 1, 1, 1],
         [-1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0, 1, 1, 1],
         [-1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 1, 1, 1, 1],
         [-1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 0, -1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, 1, -1, 1, -1, 0, -1, 1, -1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, 0, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, -1, 1, 0, 1, -1, 1, -1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, -1, 1, -1, 1, 0, 1, -1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 0, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 0, 1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, -1, 1, -1, 0, -1, 1, 1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, -1, 0, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, -1, -1, 0, 1, -1, 1, 1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, -1, -1, -1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1, 1, 1, 1]]
    print("All cases passed!")
