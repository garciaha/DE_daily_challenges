"""Distance to Nearest Vowel
Write a function that takes in a string and for each character, returns the distance 
to the nearest vowel. If the character is a vowel itself, return 0.

Examples
nearest_vowel("aaaaa") -> [0, 0, 0, 0, 0]
nearest_vowel("babbb") -> [1, 0, 1, 2, 3]

Notes
All input strings will contain at least one vowel.
Strings will be lowercased.
Vowels are: a, e, i, o, u.
"""


def nearest_vowel(word):
    pass


if __name__ == '__main__':
    assert nearest_vowel("aaaaa") == [0, 0, 0, 0, 0]
    assert nearest_vowel("babbb") == [1, 0, 1, 2, 3]
    assert nearest_vowel("abcdabcd") == [0, 1, 2, 1, 0, 1, 2, 3]
    assert nearest_vowel("shopper") == [2, 1, 0, 1, 1, 0, 1]
    print("All cases passed!")
