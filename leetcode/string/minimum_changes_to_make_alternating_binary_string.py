class MinimumChangesToMakeAlternatingBinaryString:
    def minOperations(self, s: str) -> int:
        count1 = 0
        count2 = 0
        for i, c in enumerate(s):
            if i % 2 == 0:
                if c == '1':
                    count2 += 1
                else:
                    count1 += 1
            else:
                if c == '1':
                    count1 += 1
                else:
                    count2 += 1
        return min(count1, count2)


if __name__ == '__main__':
    init = MinimumChangesToMakeAlternatingBinaryString()
    print(init.minOperations(s="0100"))  # 1
    print(init.minOperations(s="10"))  # 0
    print(init.minOperations(s="1111"))  # 2
