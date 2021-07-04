"""Centered Hexagonal Number
As stated on the On-Line Encyclopedia of Integer Sequences:

The hexagonal lattice is the familiar 2-dimensional lattice in which each point has 6 neighbors.

A centered hexagonal number is a centered figurate number that represents a hexagon with a dot in 
the center and all other dots surrounding the center dot in a hexagonal lattice.

At the end of that web page the following illustration is shown:

Illustration of initial terms:
.
.                                 o o o o
.                   o o o        o o o o o
.         o o      o o o o      o o o o o o
.   o    o o o    o o o o o    o o o o o o o
.         o o      o o o o      o o o o o o
.                   o o o        o o o o o
.                                 o o o o
.
.   1      7          19             37
.
Write a function that takes an integer n and returns "Invalid" if n is not a centered hexagonal number 
or its illustration as a multiline rectangular string otherwise.
"""


def hex_lattice(size):
    pass


if __name__ == "__main__":
    assert hex_lattice(1) == " o "
    # o
    assert hex_lattice(7) == "  o o  \n o o o \n  o o  "
    #  o o
    # o o o
    #  o o
    assert hex_lattice(
        19) == "   o o o   \n  o o o o  \n o o o o o \n  o o o o  \n   o o o   "
    #   o o o
    #  o o o o
    # o o o o o
    #  o o o o
    #   o o o
    assert hex_lattice(21) == "Invalid"
    print("All cases passed!")
