"""Crop Fields
You're given a 2D list / matrix of a crop field. Each crop needs a water source.
Each water source hydrates the 8 tiles aound it. With "w" representing a water 
source, and "c" representing a crop, is every crop hydrated?

Notes
- "w" on its own should return True, and "c" on its own should return False.
"""


def crop_hydrated(crop):
    pass


if __name__ == "__main__":
    assert crop_hydrated([
        ["w", "c"],
        ["w", "c"],
        ["c", "c"]
    ]) == True
    assert crop_hydrated([
        ["c", "c", "c"]
    ]) == False  # There isn"t even a water source.
    assert crop_hydrated([
        ["c", "c", "c", "c"],
        ["w", "c", "c", "c"],
        ["c", "c", "c", "c"],
        ["c", "w", "c", "c"]
    ]) == False
    print("All cases passed!")
