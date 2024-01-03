from typing import *


class FindMinimumInRotatedSortedArray:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        low = 0
        high = len(nums) - 1
        result = float('inf')
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid - 1
            else:
                low = mid + 1

            result = min(result, nums[mid])
        return result


if __name__ == '__main__':
    init = FindMinimumInRotatedSortedArray()
    print(init.findMin(nums=[3, 4, 5, 1, 2]))  # 1
    print(init.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))  # 0
    print(init.findMin(nums=[11, 13, 15, 17]))  # 11
