from typing import *


class EvaluateReversePolishNotation:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for t in tokens:
            if t in "+-*/":
                right = int(stack.pop())
                left = int(stack.pop())
                if t == '-':
                    stack.append(left - right)
                elif t == '+':
                    stack.append(left + right)
                elif t == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
            else:
                stack.append(t)
        return stack[-1]


if __name__ == '__main__':
    init = EvaluateReversePolishNotation()
    print(init.evalRPN(tokens=["2", "1", "+", "3", "*"]))  # 9
    print(init.evalRPN(tokens=["4", "13", "5", "/", "+"]))  # 6
    print(init.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
