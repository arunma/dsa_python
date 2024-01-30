import bisect
from typing import *


class LongestIncreasingSubsequence:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        sub = [nums[0]]

        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                i = 0
                while sub[i] < num:
                    i += 1
                sub[i] = num
        return len(sub)

    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        sub = [nums[0]]
        for num in nums[:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                ins_point = bisect.bisect_left(sub, num)
                sub[ins_point] = num
        # print(sub)
        return len(sub)


if __name__ == '__main__':
    init = LongestIncreasingSubsequence()
    print(init.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    # print(init.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # 6
    # print(init.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
