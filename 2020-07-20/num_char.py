"""Numbers First, Letters Second
Write a function that sorts list while keeping the list structure. Numbers should be first then letters both in ascending order.

Examples
num_then_char([
  [1, 2, 4, 3, "a", "b"],
  [6, "c", 5], [7, "d"],
  ["f", "e", 8]
]) -> [
  [1, 2, 3, 4, 5, 6],
  [7, 8, "a"],
  ["b", "c"], ["d", "e", "f"]
]

Notes
Test cases will containg integer and float numbers and single letters.
"""


def num_then_char(arrays):
    lengths = [len(x) for x in arrays]
    sorted_array = sum(arrays, [])
    sorted_array = sorted([x for x in sorted_array if type(x) is not str]) + sorted([x for x in sorted_array if type(x) is str])
    result = []
    for x in lengths:
        current = []
        for x in range(x):
            current.append(sorted_array.pop(0))
        result.append(current)
    return result


if __name__ == '__main__':
    assert num_then_char([
        [1, 2, 4, 3, "a", "b"],
        [6, "c", 5], [7, "d"],
        ["f", "e", 8]
    ]) == [
        [1, 2, 3, 4, 5, 6],
        [7, 8, "a"],
        ["b", "c"], ["d", "e", "f"]
    ]
    assert num_then_char([
        [1, 2, 4.4, "f", "a", "b"],
        [0], [0.5, "d", "X", 3, "s"],
        ["f", "e", 8],
        ["p", "Y", "Z"],
        [12, 18]
    ]) == [
        [0, 0.5, 1, 2, 3, 4.4],
        [8],
        [12, 18, "X", "Y", "Z"],
        ["a", "b", "d"],
        ["e", "f", "f"],
        ["p", "s"]
    ]
    print("All cases passed!")
