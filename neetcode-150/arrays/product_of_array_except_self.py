from typing import *


class ProductOfArrayExceptSelf:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     N = len(nums)
    #
    #     left = [1] * N
    #     right = [1] * N
    #     for i in range(1, N):
    #         left[i] = left[i - 1] * nums[i - 1]
    #
    #     for i in reversed(range(N - 1)):
    #         right[i] = right[i + 1] * nums[i + 1]
    #
    #     result = []
    #     for i in range(N):
    #         result.append(left[i] * right[i])
    #     return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        result = [1] * N
        R = 1
        for i in range(1, N):
            R = R * nums[i - 1]
            result[i] = R
        R = 1
        for i in reversed(range(N - 1)):
            R = R * nums[i + 1]
            result[i] *= R

        return result


if __name__ == '__main__':
    init = ProductOfArrayExceptSelf()
    print(init.productExceptSelf(nums=[1, 2, 3, 4]))  # [24,12,8,6]
    print(init.productExceptSelf(nums=[-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
    print(init.productExceptSelf(nums=[1, 2]))  # [2,1]
