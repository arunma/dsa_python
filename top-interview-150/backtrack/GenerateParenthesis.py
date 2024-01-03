from typing import *


class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack(n, result, '', 0, 0)
        return result

    def backtrack(self, n, result, curr, open, close):
        if len(curr) == 2 * n:
            result.append(curr)
            return

        if open < n:
            self.backtrack(n, result, curr + '(', open + 1, close)
        if close < open:
            self.backtrack(n, result, curr + ')', open, close + 1)


if __name__ == '__main__':
    init = GenerateParenthesis()
    print(init.generateParenthesis(n=3))  # ["((()))","(()())","(())()","()(())","()()()"]
    print(init.generateParenthesis(n=1))  # ["()"]
