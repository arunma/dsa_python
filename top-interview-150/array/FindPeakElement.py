from typing import *


class FindPeakElement:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        if N == 1:
            return 0
        elif N == 2:
            return 0 if nums[0] > nums[1] else 1

        low = 0
        high = N - 1

        while low <= high:
            mid = low + (high - low) // 2
            if (mid - 1 < 0 or nums[mid - 1] < nums[mid]) and (mid + 1 >= N or nums[mid] > nums[mid + 1]):
                return mid
            elif nums[mid - 1] > nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    init = FindPeakElement()
    print(init.findPeakElement(nums=[1, 2, 3, 1]))  # 2
    print(init.findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4]))  # 1 or 5
    print(init.findPeakElement(nums=[1]))  # 0
    print(init.findPeakElement(nums=[1, 2, 3]))  # 0
