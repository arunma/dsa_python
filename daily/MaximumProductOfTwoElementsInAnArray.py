from typing import *


class MaximumProductOfTwoElementsInAnArray:
    # def maxProduct(self, nums: List[int]) -> int:
    #     N = len(nums)
    #     maxp = float('-inf')
    #     for i in range(N - 1):
    #         for j in range(i + 1, N):
    #             maxp = max(maxp, (nums[i] - 1) * (nums[j] - 1))
    #     return maxp

    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = float('-inf')
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        return (max1 - 1) * (max2 - 1)


if __name__ == '__main__':
    init = MaximumProductOfTwoElementsInAnArray()
    print(init.maxProduct(nums=[3, 4, 5, 2]))  # 12
    print(init.maxProduct(nums=[1, 5, 4, 5]))  # 16
    print(init.maxProduct(nums=[3, 7]))  # 12
