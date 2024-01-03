class NumberOf1Bits:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 1
            n = n >> 1
        return count


if __name__ == '__main__':
    init = NumberOf1Bits()
    print(init.hammingWeight(n=11))  # 3
    print(init.hammingWeight(n=128))  # 1
