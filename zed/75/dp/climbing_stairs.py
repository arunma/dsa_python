from typing import *


class ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for step in range(2, n):
            dp[step] = dp[step - 1] + dp[step - 2]
        return dp[-1]


if __name__ == "__main__":
    init = ClimbingStairs()
    print(init.climbStairs(2))  # 2
    print(init.climbStairs(3))  # 3
