from collections import deque


class BasicCalculator:
    def calculate(self, s: str) -> int:
        queue = deque(s.replace(' ', ''))
        return self.helper(queue)

    def helper(self, queue) -> int:
        oper = '+'
        num = 0
        stack = []

        while queue:
            c = queue.popleft()
            if c in '0123456789':
                num = (num * 10) + int(c)
            if c == '(':
                sub = self.helper(queue)
                stack.append(sub)
            if c in "+-/*" or not queue:
                if oper == '+':
                    stack.append(num)
                elif oper == '-':
                    stack.append(-num)
                elif oper == '*':
                    prev = stack.pop()
                    stack.append(prev * num)
                elif oper == '/':
                    prev = stack.pop()
                    stack.append(prev / num)
                oper = c
                num = 0
            if c == ')':
                stack.append(num)
                break
        return sum(stack)


if __name__ == '__main__':
    init = BasicCalculator()
    # print(init.calculate("(1 * 1)"))  # 2
    # print(init.calculate("1 + 1"))  # 2
    # print(init.calculate(" 2-1 + 2 "))  # 3
    print(init.calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
