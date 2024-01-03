from collections import Counter
from typing import *


class ApplyOperationsToMaximizeFrequencyScore:
    # def maxFrequencyScore(self, nums: List[int], k: int) -> int:
    #     nums.sort()
    #     N = len(nums)
    #     result = 0
    #     M = N // 2
    #     median = (nums[M - 1] + nums[M]) // 2
    #     lower_bound = self.lower_bound(nums, median)
    #     upper_bound = self.upper_bound(nums, median)
    #     print(lower_bound, upper_bound)
    #     for i in range(N):

    # use binary search to find numbers closest to median
    # find the cost of each number to be equal to it
    # find the minimum cost

    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # start from num at index 0 and increment 1 (try all integers) and end at last num and find the cost of each number to be equal to it
        # find the minimum cost
        counter = Counter(nums)
        N = len(nums)
        count = 0
        for pivot in nums:
            cost = 0
            for num in nums:
                cost += abs(num - pivot)
                print(f"num:{num}, pivot:{pivot} --> cost {cost}")
                if cost < k:
                    count += 1
                if count == k:
                    return count
        return -1

    # def lower_bound(self, nums, val):
    #     low = 0
    #     high = len(nums) - 1
    #     while low <= high:
    #         mid = low + (high - low) // 2
    #         if nums[mid] <= val:
    #             low = mid + 1
    #         else:
    #             high = mid - 1
    #     return low
    #
    # def upper_bound(self, nums, val):
    #     low = 0
    #     high = len(nums) - 1
    #     while low <= high:
    #         mid = low + (high - low) // 2
    #         if nums[mid] <= val:
    #             low = mid + 1
    #         else:
    #             high = mid - 1
    #     return low


if __name__ == '__main__':
    init = ApplyOperationsToMaximizeFrequencyScore()
    print(init.maxFrequencyScore(nums=[1, 2, 6, 4], k=3))  # 3
    print(init.maxFrequencyScore(nums=[1, 4, 4, 2, 4], k=0))  # 3
