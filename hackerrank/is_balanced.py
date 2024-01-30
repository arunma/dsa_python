def isBalanced(s):
    stack = []
    mapp = {"}": "{", "]": "[", ")": "("}
    for c in s:
        if c not in "[({":
            if stack and mapp[c] == stack[-1]:
                stack.pop()
            else:
                return "NO"
        else:
            stack.append(c)
    return "YES"


if __name__ == '__main__':
    isBalanced("{[()]}")
    isBalanced("{[(])}")
    isBalanced("{{[[(())]]}}")
