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


def adj_list(pos, board):
    a = pos[0]
    b = pos[1]
    return [ (a + x, b + y) for x in range(-1, 2) for y in range(-1, 2) if (x == 0 or y == 0) and (a + x >= 0 and a + x < len(board[0]) and b + y >= 0 and b + y < len(board))]

def trace_word_path(word, board):
    letter_pos = dict((x, []) for x in word)
    for x in range(0, len(board)):
        for y in range(0, len(board[x])):
            if board[x][y] in letter_pos.keys():
                letter_pos[board[x][y]].append((x, y))
    
    if 0 in [len(letter_pos[word[i]]) for i in range(len(word))]:
        return "Not present"
    if (0, 0) not in letter_pos[word[0]]:
        return "Not present"

    path = []
    queue = [(0, 0)]
    parent = {(0, 0): "None"}
    i = 0 
    
    while len(queue) > 0:
        current = queue.pop(0)
        adj = [x for x in adj_list(current, board) if i + 1 < len(word) and x in letter_pos[word[i + 1]]]
        if len(adj) == 0 and i != len(word) - 1:
            del parent[current]
            continue
        elif i + 1 >= len(word):
            break
        for next in adj:
            if next not in parent:
                queue.append(next)
                parent[next] = current
                
                if next in letter_pos[word[i + 1]]:
                    i += 1   
                if i == len(word):
                    break  
    
    current = [x for x in letter_pos[word[i]] if x in parent][0]
    path.append(current)
    while current != (0,0):
        path.insert(0, parent[current])
        current = parent[current]
    return path

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
