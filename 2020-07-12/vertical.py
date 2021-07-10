"""Vertical Text
Create a function that converts a string into a matrix of characters that
can be read vertically. Add spaces when characters are missing.

vertical_txt("Holy bananas") -> [
  ["H", "b"],
  ["o", "a"],
  ["l", "n"],
  ["y", "a"],
  [" ", "n"],
  [" ", "a"],
  [" ", "s"]
]
"""


def vertical_txt(message):
    lengths = [len(word) for word in message.split()]
    result = []
    for x in range(0, max(lengths)):
        result.append([word[x] if len(word) > x else " " for word in message.split()])
    return result

if __name__ == '__main__':
    assert vertical_txt("Holy bananas") == [
        ["H", "b"],
        ["o", "a"],
        ["l", "n"],
        ["y", "a"],
        [" ", "n"],
        [" ", "a"],
        [" ", "s"]
    ]
    assert vertical_txt("Hello fellas") == [
        ["H", "f"],
        ["e", "e"],
        ["l", "l"],
        ["l", "l"],
        ["o", "a"],
        [" ", "s"]
    ]
    print("All cases passed!")
