"""Eadibitan
You're creating a conlang called Eadibitan. But you're too lazy to come up with your own phonology, 
grammar and orthography. So you've decided to automatize the proccess.

Write a function that translates an English word into Eadibitan.

English syllables should be analysed according to the following rules:

- Syllables will follow the pattern (C)(C)V(V(V))(C), where C is a consonant and V is a vowel. 
  Parentheses indicate that an element is optional.
- The pattern CVCV will be analyzed as CV-CV.
- The pattern CVCCV will be analyzed as CVC-CV
- The pattern CVCCCV will be analyzed as CVC-CCV
- Two or three consecutive vowels will always form a diphthong and a triphthong respectively. 
  Meaning they will be grouped in the same syllable.
- A y should be analyzed as a consonant if followed by a vowel, and as a vowel otherwise.

The order of the letters of each syllable should be altered according to the following table:

English             Eadibitan
c1 v1	            v1 c1
c1 v1 v2	        v1 c1 v2
c1 v1 v2 v3	        v1 c1 v2 v3
c1 v1 c2	        v1 c1 c2
c1 v1 v2 c2	        v1 c1 v2 c2
c1 v1 v2 v3 c2	    v1 c1 v2 v3 c2
c1 c2 v1	        c2 v1 c1
c1 c2 v1 v2	        c2 v1 c1 v2
c1 c2 v1 v2 v3	    c2 v1 c1 v2 v3
c1 c2 v1 c3	        c2 v1 c1 c3
c1 c2 v1 v2 c3	    c2 v1 c1 v2 c3
c1 c2 v1 v2 v3 c3	c2 v1 c1 v2 v3 c3

Any other pattern should be left untouched.

Notes:
- You can expect only lower case single words as arguments.
- Bonus: Try to solve it using RegEx.

"""


def eadibitan(word):
    pass


if __name__ == "__main__":
    assert eadibitan("edabitian") == "eadibitan"
    assert eadibitan("star") == "tasr"
    assert eadibitan("beautiful") == "ebauitufl"
    assert eadibitan("statistically") == "tasittisaclyl"
    print("All cases passed!")
