from functools import lru_cache
from typing import *


class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2:
            return max(nums)
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])

        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        return self.rob_inner(nums, len(nums) - 1)

    def rob_inner(self, nums, index):
        if index < 0:
            return 0
        if index == 0:
            return nums[index]

        pick = nums[index] + self.rob_inner(nums, index - 2)
        not_pick = self.rob_inner(nums, index - 1)
        max_len = max(pick, not_pick)
        return max_len

    # def rob(self, nums: List[int]) -> int:
    #
    #     @lru_cache(None)
    #     def rob_inner(index):
    #         if index == len(nums):
    #             return 0
    #         if index < 2:
    #             return nums[index]
    #
    #         max_len = max(nums[index] + rob_inner(index - 2), rob_inner(index - 1))
    #         return max_len
    #
    #     return rob_inner(len(nums) - 1)


if __name__ == "__main__":
    init = HouseRobber()
    print(init.rob([1, 2, 3, 1]))  # 4
    print(init.rob([2, 7, 9, 3, 1]))  # 12
    print(init.rob([2, 1, 1, 2]))  # 4
