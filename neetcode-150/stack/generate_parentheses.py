from typing import *


class GenerateParentheses:
    def generateParenthesis_bt(self, n: int) -> List[str]:
        result = []
        self.backtrack("", n, 0, 0, result)
        return result

    def backtrack(self, curr, n, left, right, result):
        if len(curr) == (2 * n):
            result.append(curr)
            return

        if left < n:
            self.backtrack(curr + '(', n, left + 1, right, result)
        if right < left:
            self.backtrack(curr + ')', n, left, right + 1, result)

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [("(", 1, 0)]
        while stack:
            curr, left, right = stack.pop()
            if right > left or left > n or right > n:
                continue
            if left == right == n:
                result.append(curr)
            stack.append((curr + '(', left + 1, right))
            stack.append((curr + ')', left, right + 1))

        return result


if __name__ == '__main__':
    init = GenerateParentheses()
    print(init.generateParenthesis(n=3))  # ["((()))","(()())","(())()","()(())","()()()"]
    print(init.generateParenthesis(n=1))  # ["()"]
