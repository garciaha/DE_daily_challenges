""" Parentheses Clusters
Write a function that groups a string into parentheses cluster. Each cluster should be balanced.

Example:    
split_cluster("()()()") -> ["()", "()", "()"]
split_cluster("((()))") -> ["((()))"]

All input strings will only contain parentheses.
Balanced: Every opening parens ( must exist with its matching closing parens ) in the same cluster.
"""


def split_cluster(cluster):
    paren_map = {"(": 1, ")": -1}
    clusters = []
    c = ""
    status = 0
    for symbol in cluster:
        status += paren_map[symbol]
        c += symbol
        if status == 0 and c != "":
            clusters.append(c)
            c = ""
    return clusters


if __name__ == '__main__':
    assert split_cluster("()()()") == ["()", "()", "()"]
    assert split_cluster("((()))") == ["((()))"]
    assert split_cluster("((()))(())()()(()())") == [
        "((()))", "(())", "()", "()", "(()())"]
    assert split_cluster("((())())(()(()()))") == ["((())())", "(()(()()))"]
    print("All cases passed!")
