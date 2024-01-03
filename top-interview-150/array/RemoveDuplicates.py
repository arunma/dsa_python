from typing import *


class RemoveDuplicates:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 1

        i = 1

        while i < len(nums):
            if nums[i] == nums[i - 1]:
                del nums[i]
            else:
                i += 1
        return i


if __name__ == '__main__':
    init = RemoveDuplicates()
    print(init.removeDuplicates([1,1,2])) #2
    print(init.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) #5
