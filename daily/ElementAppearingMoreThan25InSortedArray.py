from typing import *


class ElementAppearingMoreThan25InSortedArray:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        target = N / 4
        candidates = [arr[N // 4], arr[N // 2], arr[3 * N // 4]]
        for candidate in candidates:
            left = self.lower_bound(arr, candidate)
            right = self.upper_bound(arr, candidate) - 1
            # left = bisect_left(arr, candidate)
            # right = bisect_right(arr, candidate) - 1
            # print("----------------------------------------------------")
            # print(f"candidate = {candidate}, left ={left}, right={right}")
            # print(f"right-left :{right - left + 1}, target: {target}")
            if right - left + 1 > target:
                return candidate
        return -1

    def lower_bound(self, nums, val):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] < val:
                low = mid + 1
            else:
                high = mid - 1

        return low

    def upper_bound(self, nums, val):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] <= val:
                low = mid + 1
            else:
                high = mid - 1

        return low


if __name__ == '__main__':
    init = ElementAppearingMoreThan25InSortedArray()
    print(init.findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]))  # 6
    print(init.findSpecialInteger(arr=[1, 2, 3, 3]))  # 3
    print(init.findSpecialInteger(arr=[1, 1]))  # 1
    print(init.findSpecialInteger(arr=[1, 2, 3, 3, 4]))  # 3
    print(init.findSpecialInteger(arr=[15, 15, 21, 21, 32, 32, 33, 33, 33, 34, 35]))  # 33
