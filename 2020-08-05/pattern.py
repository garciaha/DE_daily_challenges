"""Complete the Pattern
You will be given a string that is made up of some repeated pattern of characters. However, 
one of the characters in the string will be missing and replaced by an underscore. 
Write a function that returns the missing character.

Examples
complete_pattern("ABCABCA_CAB") --> "B"

Notes
The pattern will be repeated in full at least twice, though 
one of those repetitions may contain the missing character.

The string may end in the middle of a repetition of the pattern.

The pattern will never contain an underscore.
"""


def complete_pattern(pattern):
    pass


if __name__ == "__main__":
    assert complete_pattern("ABCABCA_CAB") == "B"
    assert complete_pattern("_ABAABAABA") == "A"
    assert complete_pattern("X+X*X+X*X+X_") == "*"
    assert complete_pattern("g_tog@togatog@to") == "a"
    print("All cases passed!")
