from typing import *


class FindFirstAndLastPositionOfElementInSortedArray:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first = self.bin_search_left(nums, target)
        second = self.bin_search_left(nums, target + 1)

        if first == second:
            return [-1, -1]

        return [first, second - 1]

    def bin_search_left(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    init = FindFirstAndLastPositionOfElementInSortedArray()
    print(init.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))  # [3,4]
    print(init.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))  # [-1,-1]
    print(init.searchRange(nums=[], target=0))  # [-1,-1]
