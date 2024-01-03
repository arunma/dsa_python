from typing import *


class EvaluateReversePolishNotation:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "*/+-":
                right = stack.pop()
                left = stack.pop()

                if token == "*":
                    stack.append(left * right)
                elif token == "/":
                    stack.append(int(left / right))
                elif token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
            else:
                stack.append(int(token))
        return int(stack.pop())


if __name__ == '__main__':
    init = EvaluateReversePolishNotation()
    print(init.evalRPN(tokens=["2", "1", "+", "3", "*"]))  # 9
    print(init.evalRPN(tokens=["4", "13", "5", "/", "+"]))  # 6
    print(init.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
