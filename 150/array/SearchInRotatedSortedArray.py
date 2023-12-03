from typing import *


class SearchInRotatedSortedArray:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


if __name__ == '__main__':
    init = SearchInRotatedSortedArray()
    print(init.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))  # 4
    print(init.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))  # -1
    print(init.search(nums=[1], target=0))  # -1
