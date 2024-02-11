from typing import *


class RemoveDuplicatesFromSortedArray:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = 1
        i = 1
        while i < len(nums):
            if nums[i - 1] != nums[i]:
                nums[left] = nums[i]
                left += 1
            i += 1
        return left


if __name__ == '__main__':
    init = RemoveDuplicatesFromSortedArray()
    print(init.removeDuplicates([1, 1, 2]))  # 2
    print(init.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # 5
