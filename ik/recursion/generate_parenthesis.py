from typing import *


class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate_parens(n, 0, 0, "", result)
        return result

    def generate_parens(self, n, left, right, curr, result):
        if len(curr) == 2 * n:
            result.append(curr)
            return

        if left < right:
            self.generate_parens(n, left + 1, right, curr + '(', result)

        if right < left:
            self.generate_parens(n, left, right + 1, curr + ')', result)


if __name__ == '__main__':
    init = GenerateParenthesis()
    print(init.generateParenthesis(3))
