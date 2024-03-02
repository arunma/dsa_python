from typing import *


class HouseRobberIi:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return max(self.rob_inner(nums[1:]), self.rob_inner(nums[:-1]))

    def rob_inner(self, nums):
        N = len(nums)
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, N):
            dp[i + 1] = max(dp[i], nums[i] + dp[i - 1])
        return dp[-1]


if __name__ == "__main__":
    init = HouseRobberIi()
    print(init.rob([2, 3, 2]))  # 3
    print(init.rob([1, 2, 3, 1]))  # 4
    print(init.rob([0]))  # 0
