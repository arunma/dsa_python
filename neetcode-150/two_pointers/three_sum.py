from typing import *


class ThreeSum:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     if not nums:
    #         return []
    #     result = set()
    #     nums.sort()
    #     for i, third in enumerate(nums):
    #         # if i > 0 and nums[i] == nums[i - 1]:
    #         #     continue
    #         self.two_sum(nums[:i] + nums[i + 1:], -third, result)
    #     return result
    #
    # def two_sum(self, nums, target, result):
    #     N = len(nums)
    #     left = 0
    #     right = N - 1
    #
    #     while left < right:
    #         curr = nums[left] + nums[right]
    #         if curr == target:
    #             result.add(tuple(sorted([nums[left], nums[right], -target])))
    #             left += 1
    #             right -= 1
    #         elif curr < target:
    #             left += 1
    #         else:
    #             right -= 1
    #     return

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        nums.sort()
        for i, third in enumerate(nums):
            if third > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.two_sum(nums, i, -third, result)
        return result

    def two_sum(self, nums, ti, target, result):
        N = len(nums)
        left = ti + 1
        right = N - 1

        while left < right:
            curr = nums[left] + nums[right]
            if curr == target:
                result.append([-target, nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # right -= 1

            elif curr < target:
                left += 1
            else:
                right -= 1
        return


if __name__ == '__main__':
    init = ThreeSum()
    print(init.threeSum(nums=[-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    print(init.threeSum(nums=[]))  # []
    print(init.threeSum(nums=[0, 0, 0]))  # [[0,0,0]]
    print(init.threeSum(
        [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))  # [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
    print(init.threeSum([-2, 0, 0, 2, 2]))  # [[-2,0,2]]
