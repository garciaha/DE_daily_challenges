"""Postfix Notation (Part 2: Infix to Postfix)
Given a string representing an infix expression, return the postfix equivalent. The operands stay in their original 
order, and any parentheses are removed. Only the operator order is changed. Operands and operators will be separated 
by a single space, with the exception of parentheses (see examples).

Examples
infix_to_postfix("7 + 3") -> "7 3 +"

infix_to_postfix("(8 + 4) / 4") -> "8 4 + 4 /"

Notes
Converting infix expressions to postfix expressions is an example of operator-precedence parsing, the most famous of 
which is Dijkstra's "shunting-yard" algorithm.
"""


def infix_to_postfix(expression):
    pass


if __name__ == "__main__":
    assert infix_to_postfix("7 + 3") == "7 3 +"
    assert infix_to_postfix("(8 + 4) / 4") == "8 4 + 4 /"
    assert infix_to_postfix("4 * (5 - (7 + 2))") == "4 5 7 2 + - *"
    assert infix_to_postfix("3 + 4 ** 2") == "3 4 2 ** +"
    print("All cases passed!")
