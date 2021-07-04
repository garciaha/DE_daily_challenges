"""Conway's Game of Life

The goal of this challenge is to implement the logic used in Conway's Game of Life. 
Wikipedia will give a better understanding of what it is and how it works (check the resources tab above).

Rules
- For a space that's "populated":
  - Each cell with 0 or 1 neighbours dies, as if by solitude.
  - Each cell with 2 or 3 neighbours survives.
  - Each cell with 4 or more neighbours dies, as if by overpopulation.
  - For a space that's "empty" or "unpopulated":
  - Each cell with 3 neighbours becomes populated.

Parameters
    size_x: Size of the board for the X axis
    size_y: Size of the board for the Y axis
    board_seed: Board seed to start the iterations
                If None, create a random board seed
    generations: Number of generations to present
    interactive: True - False
                 For True, display the modification of the board with a delay of .5 secs
                 For False, just calculate the board and return the result
        
Board:
    0 means that the cell is empty.
      (Use a space for interactive display)
    1 means the cell is populated.
      (Use a * for interactive display)
"""


def game_of_life(size_x, size_y, board, generations, interactive):
    pass


if __name__ == "__main__":
    game_of_life(20, 20, None, 100, True)
    print(game_of_life(20, 20, None, 100, False))
    print("All cases passed!")
