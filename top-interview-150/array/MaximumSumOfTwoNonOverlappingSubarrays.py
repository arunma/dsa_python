from typing import *


class MaximumSumOfTwoNonOverlappingSubarrays:
    # def maxSumTwoNoOverlap(self, nums: List[int], L: int, M: int) -> int:
    #     N = len(nums)
    #     if N < L + M:
    #         return 0
    #     prefix_sum = {}
    #     curr = 0
    #     for i, num in enumerate(nums):
    #         curr += num
    #         prefix_sum[i] = curr
    #
    #     # print(prefix_sum)
    #
    #     max_l = float('-inf')
    #     max_m = float('-inf')
    #
    #     result = float('-inf')
    #     for i in range(L + M, N):
    #         max_l = max(max_l, prefix_sum[i - M] - prefix_sum[i - M - L])
    #         max_m = max(max_m, prefix_sum[i - L] - prefix_sum[i - M - L])
    #         result = max(result, max_l + prefix_sum[i] - prefix_sum[i - M], max_m + prefix_sum[i] - prefix_sum[i - L])
    #     return result

    def maxSumTwoNoOverlap(self, nums: List[int], L: int, M: int) -> int:
        if len(nums) < L + M: return 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res, maxL, maxM = nums[L + M - 1], nums[L - 1], nums[M - 1]
        for i in range(L + M, len(nums)):
            maxL = max(maxL, nums[i - M] - nums[i - M - L])
            maxM = max(maxM, nums[i - L] - nums[i - L - M])
            res = max(res, maxL + nums[i] - nums[i - M], maxM + nums[i] - nums[i - L])
        return res

    def maxSumTwoNoOverlap(self, nums: List[int], L: int, M: int) -> int:
        N = len(nums)
        if N < L + M:
            return 0

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        max_l = max_m = result = 0

        print(len(prefix))

        # M
        for i in range(M, len(prefix) - L):
            max_m = max(max_m, prefix[i] - prefix[i - M])
            result = max(result, max_m + prefix[i + L] - prefix[i])

        # L
        for i in range(L, len(prefix) - M):
            max_l = max(max_l, prefix[i] - prefix[i - L])
            result = max(result, max_l + prefix[i + M] - prefix[i])

        return result


if __name__ == '__main__':
    init = MaximumSumOfTwoNonOverlappingSubarrays()
    # print(init.maxSumTwoNoOverlap(nums=[0, 6, 5, 2, 2, 5, 1, 9, 4], L=1, M=2))
    # print(init.maxSumTwoNoOverlap(nums=[3, 8, 1, 3, 2, 1, 8, 9, 0], L=3, M=2))
    # print(init.maxSumTwoNoOverlap(nums=[2, 1, 5, 6, 0, 9, 5, 0, 3, 8], L=4, M=3))
    print(init.maxSumTwoNoOverlap(nums=[1, 0, 1], L=1, M=1))
