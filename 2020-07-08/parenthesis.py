""" Parentheses Clusters
Write a function that groups a string into parentheses cluster. Each cluster should be balanced.

Example:    
split_cluster("()()()") -> ["()", "()", "()"]
split_cluster("((()))") -> ["((()))"]

All input strings will only contain parentheses.
Balanced: Every opening parens ( must exist with its matching closing parens ) in the same cluster.
"""


def split_cluster(cluster):
    status_calc = {"(": 1, ")": -1}
    clusters = []
    current = ""
    status = 0
    for p in cluster:
        status += status_calc[p]
        current += p
        if status == 0:
            clusters.append(current)
            current = ""
    return clusters


if __name__ == '__main__':
    assert split_cluster("()()()") == ["()", "()", "()"]
    assert split_cluster("((()))") == ["((()))"]
    assert split_cluster("((()))(())()()(()())") == [
        "((()))", "(())", "()", "()", "(()())"]
    assert split_cluster("((())())(()(()()))") == ["((())())", "(()(()()))"]
    print("All cases passed!")
