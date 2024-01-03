from typing import *


class MaximumNumberOfNonOverlappingSubarraysWithSumEqualsTarget:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        prefix_sum = {0: -1}
        max_index = -1
        total = 0
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum - target in prefix_sum and prefix_sum[curr_sum - target] >= max_index:
                max_index = i
                total += 1
            prefix_sum[curr_sum] = i
        return total


if __name__ == '__main__':
    init = MaximumNumberOfNonOverlappingSubarraysWithSumEqualsTarget()
    print(init.maxNonOverlapping(nums=[1, 1, 1, 1, 1], target=2))  # 2
    print(init.maxNonOverlapping(nums=[-1, 3, 5, 1, 4, 2, -9], target=6))  # 2
    print(init.maxNonOverlapping(nums=[], target=0))
    print(init.maxNonOverlapping(nums=[0, 0, 0], target=0))  # 3
