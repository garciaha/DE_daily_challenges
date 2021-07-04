"""King's Escape
Create a function that takes a chess position (black pieces to move next) and
returns the status of the black king.

- The black king is safe if no white pieces threaten it.
- The black king is checked if one white piece threatens it and the king can escape
  to an unthreatened square.
- The black king is double-checked if two white pieces threaten it and the king can
  escape to an unthreatened square.
- The black king is checkmated if it is attacked and cannot escape.
- White pieces are represented with uppercase letters:
  Pawn P, Knight N, Bishop B, Rook R, Queen Q, King K.
  Black pieces are represented with lowercase letters.
- The program must return the possible escape positions (if they exist) as a list of
  tuples (x, y) being x, the horizontal position of the escape square, and y the
  vertical position of the escape square. The escape positions must be sorted by x
  and then y, always from the lowest value to the highest value.
- The chessboard will always have 8 rows and 8 columns. 0 <= x < 8 and 0 <= y < 8.
  The white queen starts at (7, 3).
- A stalemate occurs when a player, on their turn, has no legal moves, and the player's
  king is not in check. Stalemate is not a possibility in this challenge.
"""


def check_black_king(board):
    pass


if __name__ == "__main__":
    assert check_black_king([
        [" ", " ", " ", " ", " ", "r", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", "q"],
        [" ", " ", " ", " ", " ", " ", "N", " "],
        ["k", " ", " ", " ", " ", " ", " ", " "],
        [" ", "P", " ", "P", " ", " ", " ", " "],
        [" ", " ", "P", " ", " ", "Q", " ", " "],
        ["B", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", "R", " ", " ", "K", " "]]) == \
        "The black king is checked. Possible escape positions: [(2, 0), (2, 1), (3, 1), (4, 0)]"
    assert check_black_king([
        [" ", " ", " ", " ", " ", "r", " ", " "],
        [" ", " ", " ", " ", " ", " ", "k", "q"],
        [" ", " ", " ", " ", " ", " ", "N", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", "P", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", "Q", " ", " "],
        ["B", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", "R", " ", " ", "K", " "]]) == \
        "The black king is safe."
    assert check_black_king([
        [" ", " ", " ", " ", " ", "r", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", "q"],
        [" ", " ", " ", " ", " ", " ", "N", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", "P", " ", "k", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", "Q", " ", " "],
        ["B", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", "R", " ", " ", "K", " "]]) == \
        "The black king is checkmated."
    assert check_black_king([
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", "k", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", "B", "p", " ", " "],
        [" ", " ", " ", "q", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["p", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", "K", "R", " "]]) == \
        "The black king is double-checked. Possible escape positions: [(0, 5), (1, 5), (1, 7), (2, 7)]"
    print("All cases passed!")
