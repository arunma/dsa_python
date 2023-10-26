from typing import *


class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        N = len(nums)
        for i in range(N - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.twoSum(nums[i + 1:], -nums[i], result)
        return result

    def twoSum(self, nums, target, result):
        l = 0
        r = len(nums) - 1
        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum == target:
                result.add((- target, nums[l], nums[r]))
                l += 1
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                r -= 1
        return


if __name__ == '__main__':
    init = ThreeSum()
    # print(init.threeSum(nums=[0, 0, 0]))
    # print(init.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
    # print(init.threeSum(nums=[0, 1, 1]))
    print(init.threeSum([-2, 0, 0, 2, 2]))
