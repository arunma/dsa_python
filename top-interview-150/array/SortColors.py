from typing import *


class SortColors:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1

        one_start = 0
        while left <= right:
            if nums[left] == 0:
                nums[left], nums[one_start] = nums[one_start], nums[left]
                left += 1
                one_start += 1
            elif nums[left] == 2:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1
            else:
                left += 1


if __name__ == '__main__':
    init = SortColors()
    print(init.sortColors(nums=[2, 0, 2, 1, 1, 0]))  # [0,0,1,1,2,2]
    print(init.sortColors(nums=[2, 0, 1]))  # [0,1,2]
    print(init.sortColors(nums=[0]))  # [0]
    print(init.sortColors(nums=[1]))  # [1]
