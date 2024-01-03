from typing import *


class MaximumSubarray:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr_sum = 0
        max_sum = float('-inf')
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum


if __name__ == '__main__':
    init = MaximumSubarray()
    print(init.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(init.maxSubArray(nums=[1]))  # 1
    print(init.maxSubArray(nums=[-1]))  # -1
    print(init.maxSubArray(nums=[5, 4, -1, 7, 8]))  # 23
    print(init.maxSubArray(nums=[-5, -4, -1, -7, -8]))  # 23
