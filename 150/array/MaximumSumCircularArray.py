from typing import *


class MaximumSumCircularArray:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = 0
        max_sum = float('-inf')
        curr_min = 0
        min_sum = float('inf')

        for num in nums:
            curr_max = max(curr_max + num, num)
            curr_min = min(curr_min + num, num)
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

        alt_max = sum(nums) - min_sum
        if max_sum > 0:
            return max_sum if max_sum > alt_max else alt_max
        return max_sum


if __name__ == '__main__':
    init = MaximumSumCircularArray()
    # print(init.maxSubarraySumCircular(nums=[1, -2, 3, -2]))  # 3
    # print(init.maxSubarraySumCircular(nums=[5, -3, 5]))  # 10
    # print(init.maxSubarraySumCircular(nums=[3, -1, 2, -1]))  # 4
    # print(init.maxSubarraySumCircular(nums=[3, -2, 2, -3]))  # 3
    # print(init.maxSubarraySumCircular(nums=[-2, -3, -1]))  # -1
    print(init.maxSubarraySumCircular(nums=[-2]))  # -2
