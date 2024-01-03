from typing import *


class ThreeSumSmaller:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        if len(nums) < 3:
            return 0

        count = 0
        nums.sort()
        for i, first in enumerate(nums):
            count += self.two_sum(nums, first, target, i + 1)
        return count

    def two_sum(self, nums, first, target, i):
        low = i
        high = len(nums) - 1

        count = 0
        while low < high:
            val = first + nums[low] + nums[high]

            if val < target:
                count += high - low
                low += 1
            else:
                high -= 1

        return count


if __name__ == '__main__':
    init = ThreeSumSmaller()
    print(init.threeSumSmaller(nums=[-2, 0, 1, 3], target=2))  # 2
    print(init.threeSumSmaller(nums=[], target=0))  # 0
    print(init.threeSumSmaller(nums=[0], target=0))  # 0
