from typing import *


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return [-1, -1]

        prev = {}
        for i, num in enumerate(nums):
            if target - num in prev:
                return [prev[target - num], i]

            prev[num] = i
        return [-1, -1]


if __name__ == '__main__':
    init = TwoSum()
    print(init.twoSum(nums=[2, 7, 11, 15], target=9))  # [0, 1]
    print(init.twoSum(nums=[3, 2, 4], target=6))  # [1, 2]
    print(init.twoSum(nums=[3, 3], target=6))  # [0, 1]
