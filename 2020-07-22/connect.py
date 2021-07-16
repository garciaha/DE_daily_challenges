"""Connecting Words
Write a function that connects each previous word to the next word by the shared 
letters. Return the resulting string (removing duplicate characters in the overlap) 
and the minimum number of shared letters across all pairs of strings.

Examples
connect(["oven", "envier", "erase", "serious"]) -> ["ovenvieraserious", 2]

connect(["move", "over", "very"]) -> ["movery", 3]

connect(["to", "ops", "psy", "syllable"]) -> ["topsyllable", 1]

# "to" and "ops" share "o" (1)
# "ops" and "psy" share "ps" (2)
# "psy" and "syllable" share "sy" (2)
# the minimum overlap is 1

connect(["aaa", "bbb", "ccc", "ddd"]) -> ["aaabbbcccddd", 0]

Notes
More specifically, look at the overlap between the previous words ending letters and the next word's beginning letters.
"""

def connect(words):
    shared = []
    connected = words[0]
    for x in range(1, len(words)):
        start = words[x][0]
        end = words[x-1][-1]
        last = words[x-1][::-1]
        spos = last.find(start)
        epos = words[x].find(end)

        if start in words[x-1] and end in words[x] and last[:spos+1][::-1] == words[x][:epos+1]:
            shared.append(epos+1)
            connected += words[x][epos+1:]    
        else:
            shared.append(0)
            connected += words[x]

    return [connected, min(shared)] 


if __name__ == '__main__':
    assert connect(["oven", "envier", "erase", "serious"]) == [
        "ovenvieraserious", 2]
    assert connect(["move", "over", "very"]) == ["movery", 3]
    assert connect(["to", "ops", "psy", "syllable"]) == ["topsyllable", 1]
    assert connect(["silver", "version", "onerous", "usa", "apple", "please"]) == [
        "silversionerousapplease", 1]
    print("All cases passed!")
