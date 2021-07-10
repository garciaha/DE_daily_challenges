"""Columnar Cipher
The columnar cipher is a transposition cipher that works like this.

Start with a secret message:

msg = "Meet me by the lake at midnight. Bring shovel."
Transform uppercase letters into lowercase and remove punctuation and spaces:

msg = "meetmebythelakeatmidnightbringshovel"
Then, pick a keyword made out of distinct letters:

keyword = "python"
Break up the message into chunks of the same length as the keyword, and write them in rows under the keyword. 
Then, number the columns based on the alphabetised order of the letters in the keyword:

p	y	t	h	o	n
m	e	e	t	m	e
b	y	t	h	e	l
a	k	e	a	t	m
i	d	n	i	g	h
t	b	r	i	n	g
s	h	o	v	e	l
4	6	5	1	3	2

Read off the enciphered message (ciphertext) from the columns, in the order specified by the numbers:

ciphertext = "thaiivelmhglmetgnembaitsetenroeykdbh"

If the message length is not a multiple of the keyword length, fill in each blank space with "x". For example:

msg = "Meet me at midnight."

keyword = "python"
p	y	t	h	o	n
m	e	e	t	m	e
a	t	m	i	d	n
i	g	h	t	x	x

Create a function that takes a string and a keyword. Return the ciphertext if the string is in plaintext 
(i.e. broken up into normal English words and punctuated), or the deciphered message if the string is in 
ciphertext. The resulting deciphered message will not have spaces
"""
"""
m	o	n	t	y
m	e	e	t	m
e	b	y	t	h
e	l	a	k	e
a	t	m	i	d	
n	i	g	h	t
b	r	i	n	g	
s	h	o	v	e	
l	x	x	x	x
1	3	2	4	5
"""

def cipher(msg, keyword):
    cypher = dict((sorted(keyword)[i], msg[i*int(len(msg)/len(keyword)):(i+1)*int(len(msg)/len(keyword))]) for i in range(len(keyword)))
    result = ""
    for y in range(int(len(msg)/len(keyword))):
        for x in keyword:
            result += cypher[x][y]
    return result

def c_cipher(msg, keyword):
    stripped = "".join([char.lower() for word in msg.split() for char in word if char.isalpha()])
    if stripped == msg:
        return cipher(stripped, keyword)
    if len(stripped) % len(keyword) != 0:
        stripped += "x" * (len(keyword) - (len(stripped) % len(keyword)))
    cypher = dict((keyword[i], [stripped[i + len(keyword)*x] for x in range(int(len(stripped) / len(keyword)))]) for i in range(len(keyword)))
    result = ""
    for key in sorted(cypher.keys()):
        result += "".join(cypher[key])
    return result

if __name__ == '__main__':

    assert c_cipher("Meet me by the lake at midnight. Bring shovel.",
                    "python") == "thaiivelmhglmetgnembaitsetenroeykdbh"
    assert c_cipher("meeanbsleyamgioxebltirhxttkihnvxmhedtgex",
                    "monty") == "meetmebythelakeatmidnightbringshovelxxxx"
    assert c_cipher("Mission Delta Kilo Sierra has been compromised. Kill Steve. Evacuate",
                    "cake") == "ioliiabcrsiteuxmieksrsnpiksecesdaoraemmdlvatxsntleheooelevax"
    print("All cases passed!")
