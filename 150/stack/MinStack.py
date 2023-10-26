class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        mini = val
        if self.min_stack:
            mini = min(val, self.min_stack[-1])
        self.min_stack.append(mini)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    init = MinStack()
    print(init.push(-2))  # None
    print(init.push(0))  # None
    print(init.push(-3))  # None
    print(init.getMin())  # -3
    print(init.pop())  # None
    print(init.top())  # 0
    print(init.getMin())  # -2
