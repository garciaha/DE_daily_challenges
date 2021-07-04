"""Hidden Word

Within the following URL is a hidden word.

http://www.pythonchallenge.com/pc/def/ocr.html

Use your coding python skills to detect it ...

Instructions - call python 'TEXT' with the text to be decoded in between single quotes
"""


def decode(url):
    pass


if __name__ == "__main__":
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    assert decode(url) == "equality"
    print("All cases passed!")
