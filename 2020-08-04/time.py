"""
Character Recognition - What's the Time?
As a programmer in a forensic laboratory, you have been asked to write a function to decode a bitmap image of a digital 
clock to determine what time it was when the image was created. The bitmap image has been converted to a string of binary 
digits 0 or 1 where 0 represents a white background pixel and 1 represents a black pixel. You must convert this binary 
string into a time in hours and minutes in the form hh:mm (e.g. 09:47).

The clock face shows the time in a black on white background where each character is three cells wide and five cells deep. 
Notice there is a space between the numbers represented by a column of blank cells:

See:
2135.png
0647.png
1859.png

Each image is 17 bits wide by 5 bits deep. Each row is encoded as a 17 character string of 1s and 0s and the five rows 
are then concatenated into an 85 character string which is passed to your function. For example, the above image is encoded as follows:

row 1 = "11100100001110111"
row 2 = "10101100100010100"
row 3 = "10100100001110111"
row 4 = "10100100100010001"
row 5 = "11101110001110111"

bitmap -> "1110010000111011110101100100010100101001000011101111010010010001000111101110001110111"
If you examine the above rows maps carefully, you should be able to see the clock digits in the pattern of 1, 
The first three columns show the number 0, this is followed by a column of all 0 representing a space between the numbers, 
then comes another three columns representing the number 1, then three columns representing the character :, then three 
columns representing 3, a column of zeroes representing a space and finally three columns representing the number 5. 
The resulting time is 01:35.

Notes
There are no errors in the encoding, so you don't need to check for near matches.

"""


def whats_the_time(bitmap):
    pass


if __name__ == "__main__":
    assert whats_the_time(
        "1110010000111011110101100100010100101001000011101111010010010001000111101110001110111") == "01:35"
    assert whats_the_time(
        "1110010000101011100101100101010001111001000011100011000010010001000111101110000010001") == "21:47"
    print("All cases passed!")
