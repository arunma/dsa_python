class ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climb_stairs(0, n, memo)

    def climb_stairs(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1

        if i not in memo:
            memo[i] = self.climb_stairs(i + 1, n, memo) + self.climb_stairs(i + 2, n, memo)
        return memo[i]


if __name__ == '__main__':
    init = ClimbingStairs()
    print(init.climbStairs(n=2))  # 2
    print(init.climbStairs(n=3))  # 3
    print(init.climbStairs(n=5))  # 8
