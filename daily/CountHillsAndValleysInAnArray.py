from typing import *


class CountHillsAndValleysInAnArray:
    # def countHillValley(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     N = len(nums)
    #     result = 0
    #     previous = nums[0]
    #     for i in range(1, N - 1):
    #         if previous < nums[i] and nums[i] > nums[i + 1] or previous > nums[i] and nums[i] < nums[i + 1]:
    #             previous = nums[i]
    #             result += 1
    #     return result

    def countHillValley(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        result = 0
        previous = nums[0]
        for i in range(1, N - 1):
            if previous < nums[i] > nums[i + 1] or previous > nums[i] < nums[i + 1]:
                result += 1
                previous = nums[i]

        return result


if __name__ == '__main__':
    init = CountHillsAndValleysInAnArray()
    # print(init.countHillValley(nums=[2, 4, 1, 1, 6, 5]))  # 3
    # print(init.countHillValley(nums=[6, 6, 5, 5, 4, 1]))  # 0
    print(init.countHillValley(nums=[6, 5, 2, 2, 5]))
