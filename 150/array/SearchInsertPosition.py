from typing import *


class SearchInsertPosition:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == '__main__':
    init = SearchInsertPosition()
    print(init.searchInsert(nums=[1, 3, 5, 6], target=5))  # 2
    print(init.searchInsert(nums=[1, 3, 5, 6], target=2))  # 1
    print(init.searchInsert(nums=[1, 3, 5, 6], target=7))  # 4
    print(init.searchInsert(nums=[1, 3, 5, 6], target=0))  # 0
    print(init.searchInsert(nums=[1], target=0))  # 0
