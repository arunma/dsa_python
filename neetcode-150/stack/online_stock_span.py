class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        days = 1
        while self.stack and price >= self.stack[-1][0]:
            old_price, d = self.stack.pop()
            days += d
        self.stack.append((price, days))
        return days


if __name__ == '__main__':
    init = StockSpanner()
    print(init.next(100))  # 1
    print(init.next(80))  # 1
    print(init.next(60))  # 1
    print(init.next(70))  # 2
    print(init.next(60))  # 1
    print(init.next(75))  # 4
    print(init.next(85))  # 6
