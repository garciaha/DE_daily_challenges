"""Say the Number!
Create a function that takes a numeral (just digits without separators (e.g. 19093 instead of 19,093)
and returns the standard way of reading a number, complete with punctuation.

Notes
Must read any number from 0 to 999,999,999,999,999.
"""


def say_it(number):
    pass


if __name__ == '__main__':
    assert say_it(0) == "Zero."
    assert say_it(11) == "Eleven."
    assert say_it(
        1043283) == "One million, forty three thousand, two hundred and eighty three."
    assert say_it(
        90376000010012) == "Ninety trillion, three hundred and seventy six billion, ten thousand and twelve."
    print("All cases passed!")
