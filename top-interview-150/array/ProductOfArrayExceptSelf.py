from typing import *


class ProductOfArrayExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1] * N
        suffix = [1] * N

        for i in range(1, N):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(N - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        result = [0] * N

        for i in range(N):
            result[i] = prefix[i] * suffix[i]

        return result


if __name__ == '__main__':
    init = ProductOfArrayExceptSelf()
    init.productExceptSelf([1, 2, 3, 4])  # [24,12,8,6]
