import sys
from typing import *


class MinimumSizeSubarraySum:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ws = 0
        curr_sum = 0
        min_length = sys.maxsize

        for we in range(len(nums)):
            curr_sum += nums[we]
            while curr_sum >= target:
                min_length = min(min_length, we - ws + 1)
                curr_sum -= nums[ws]
                ws += 1

        if min_length == sys.maxsize:
            return 0

        return min_length


if __name__ == '__main__':
    init = MinimumSizeSubarraySum()
    print(init.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))  # 2
    print(init.minSubArrayLen(target=4, nums=[1, 4, 4]))  # 1
    print(init.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))  # 0
