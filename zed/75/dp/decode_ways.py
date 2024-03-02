from typing import *


class DecodeWays:
    def numDecodings(self, s: str) -> int:
        return self.num_decodings(s, 0, {})

    def num_decodings(self, s, i, memo):
        if i in memo:
            return memo[i]
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        max_ways = 0
        max_ways += self.num_decodings(s, i + 1, memo)
        if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
            max_ways += self.num_decodings(s, i + 2, memo)
        memo[i] = max_ways
        return max_ways

    # def numDecodings(self, s: str) -> int:
    #     return self.num_decodings(s, {})
    #
    # def num_decodings(self, s, memo):
    #     if s in memo:
    #         return memo[s]
    #     if not s:
    #         return 1
    #     if s[0] == '0':
    #         return 0
    #     max_ways = 0
    #     max_ways += self.num_decodings(s[1:], memo)
    #     if len(s) >= 2 and int(s[0:2]) <= 26:
    #         max_ways += self.num_decodings(s[2:], memo)
    #     memo[s] = max_ways
    #     return max_ways


if __name__ == "__main__":
    init = DecodeWays()
    print(init.numDecodings("27"))  # 1
    print(init.numDecodings("12"))  # 2
    print(init.numDecodings("226"))  # 3
    print(init.numDecodings("0"))  # 0
    print(init.numDecodings("06"))  # 0
