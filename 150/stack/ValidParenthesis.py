class ValidParenthesis:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in "[{(":
                stack.append(c)
            elif not stack or stack.pop() != map[c]:
                return False
        return not stack


if __name__ == '__main__':
    init = ValidParenthesis()
    print(init.isValid(s="()"))  # True
    print(init.isValid(s="()[]{}"))  # True
    print(init.isValid(s="(]"))  # False
