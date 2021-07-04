"""Find All Prime Numbers in Decimal Integer
Create a function that takes an integer argument and returns a list of prime numbers found in the 
decimal representation of that number.

For example, extract_primes(1717) returns [7, 7, 17, 17, 71].

The list should be in acending order. If a prime number appears more than once, every occurance
should be listed. If no prime numbers are found, return an empty list.

All test cases are positive real integers.
Some numbers will have leading zeros. 
For example, the number 103 contains the prime number 3, but also contains 03. 
These should be treated as the same number, so the result would simply be [3].
"""


def extract_primes(number):
    pass


if __name__ == '__main__':
    assert extract_primes(1) == []
    assert extract_primes(7) == [7]
    assert extract_primes(73) == [3, 7, 73]
    # The following test was mpdified from [3] to [3, 103]
    assert extract_primes(103) == [3, 103]
    assert extract_primes(1313) == [3, 3, 13, 13, 31, 131, 313]
    print("All cases passed!")
