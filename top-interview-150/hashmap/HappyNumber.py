class HappyNumber:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n > 0:
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n = n // 10
            if s in seen:
                return False
            elif s == 1:
                return True
            seen.add(s)
            n = s
        return False


if __name__ == '__main__':
    init = HappyNumber()
    print(init.isHappy(n=19))  # true
    print(init.isHappy(n=2))  # false
    print(init.isHappy(n=1111111))  # true
