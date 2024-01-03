from typing import *


class ContainsDuplicate:
    def contains_duplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


if __name__ == '__main__':
    init = ContainsDuplicate()
    print(init.contains_duplicate(nums=[1, 2, 3, 1]))  # True
