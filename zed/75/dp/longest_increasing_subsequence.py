import bisect
from functools import lru_cache
from typing import *


class LongestIncreasingSubsequence:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     N = len(nums)
    #     dp = [1] * N
    #     for i in range(1, N):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        max_length = 1
        for i in range(len(nums)):
            max_length = max(max_length, self.length_of_lis(nums, i))
        return max_length

    def length_of_lis(self, nums, i):
        length = 1
        for j in range(i):
            if nums[j] < nums[i]:
                length = max(length, 1 + self.length_of_lis(nums, j))
        return length

    def lengthOfLIS(self, nums: List[int]) -> int:
        subs = [nums[0]]
        for num in nums:
            if num > subs[-1]:
                subs.append(num)
            else:
                iloc = bisect.bisect_left(subs, num)
                subs[iloc] = num
        return len(subs)

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     @lru_cache(None)
    #     def length_of_lis(i):
    #         length = 1
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 length = 1 + length_of_lis(j)
    #         return length
    #
    #     max_length = 1
    #     for i in range(len(nums)):
    #         max_length = max(max_length, length_of_lis(i))
    #     return max_length

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     N = len(nums)
    #     max_length = 1
    #     for i in range(N):
    #         max_length = max(max_length, self.lis_recursive(i, nums))
    #     return max_length
    #
    # def lis_recursive(self, i, nums):
    #     if i == 0:
    #         return 1
    #     max_length = 1
    #     for j in range(i):
    #         if nums[i] > nums[j]:
    #             max_length = max(max_length, self.lis_recursive(j, nums) + 1)
    #     return max_length


if __name__ == "__main__":
    init = LongestIncreasingSubsequence()
    print(init.lengthOfLIS([1, 4, 6, 2]))  # 4
    print(init.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
    print(init.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    print(init.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
    print(init.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
