"""Longest Alternating Substring
Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. 
If two or more substrings have the same length, return the substring that occurs first.

Examples
longest_substring("225424272163254474441338664823") -> "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

The minimum alternating substring size is 2.
"""


def longest_substring(input):
    pass


if __name__ == '__main__':
    assert longest_substring("225424272163254474441338664823") == "272163254"
    assert longest_substring("594127169973391692147228678476") == "16921472"
    assert longest_substring("721449827599186159274227324466") == "7214"
    print("All cases passed!")
