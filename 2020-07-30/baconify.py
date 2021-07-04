"""Hidden in Plain Sight
This challenge makes use of a modified Baconian (Francis Bacon) cipher. 

The following is an example of a (modified) Baconian ciphertext:

ciphertext = "KNowlEDgE ITsElf Is power."
The peculiar capitalisation might, at first glance, suggest that either the lowercase or uppercase 
letters contain, or code for, the hidden message (upper = "KNEDEITEI", lower = "owlgslfspower").

But actually, the Baconian cipher is a steganographic method of hiding information. The hidden message 
is not in the content of the ciphertext, but rather in the presentation. It doesn't matter which letters 
are capitalised, just the order of the capitalisation.

To decipher the ciphertext above, remove spaces and punctuation, then cleave the message into chunks of 
length 5, leaving out the remainder:

ciphertext = "KNowl EDgEI TsElf Ispow"

Each chunk represents a letter. Decipher them according to the following 
table ("u" means uppercase, "l" means lowercase):

Letter	Pattern
a	uuuuu
b	uuuul
c	uuulu
d	uuull
e	uuluu
f	uulul
g	uullu
h	uulll
i	uluuu
j	uluul
k	ululu
l	ulull
m	ulluu
n	ullul
o	ulllu
p	ullll
q	luuuu
r	luuul
s	luulu
t	luull
u	luluu
v	lulul
w	lullu
x	lulll
y	lluuu
z	lluul
.	llllu
(space) lllll

deciphered = "help"
Create a function that takes 1 or 2 arguments:

A Baconian ciphertext or a plaintext message to be enciphered: msg.
A background text in which the message is to be hidden: mask.
If only one argument is given (ciphertext), return the deciphered message (in lowercase, with spaces and full stops as encoded).

If a second argument is given, encipher the first argument msg into the mask, and return the resulting ciphertext. When enciphering, encipher full stops and spaces along with the words. Disregard the rest. The ciphertext itself should retain all the punctuation and spaces of the original mask.
"""

table = {"12345": "a", "1234": "b", "1235": "c", "123": "d", "1245": "e", "124": "f", "125": "g", "12": "h", "1345": "i", "134": "j", "135": "k", "13": "l", "145": "m",
         "14": "n", "15": "o", "1": "p", "2345": "q", "234": "r", "235": "s", "23": "t", "245": "u", "24": "v", "25": "w", "2": "x", "345": "y", "45": "z", "5": ".", "": " "}


def baconify(message, *mask):
    pass


if __name__ == "__main__":
    assert baconify("KNowlEDgE ITsElf Is power.") == "help"
    assert baconify(
        "Help me.", "Man prefers to believe what he prefers to be true.") == "MAn prEFeRS To BelIeve what he PreFERS tO Be truE."
    # Both the space (between "help" and "me") and the full stop at the end are enciphered.
    assert baconify(
        "Help!!!", "Knowledge itself is power.") == "KNowlEDgE ITsElf Is power."
    # Exclamation marks not enciphered, so the resulting ciphertext is identical to the first example.
    print("All cases passed!")
