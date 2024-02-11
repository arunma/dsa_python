from typing import List


class PartitionEqualSubsetSum:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ & 1:
            return False
        return self.can_partition(nums, summ // 2)

    def can_partition(self, nums, target):
        if target == 0:
            return True

        for i in range(len(nums)):
            # pick or skip
            if self.can_partition(nums[i + 1:], target - nums[i]) or self.can_partition(nums[i + 1:], target):
                return True
        return False

    # Memo
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ & 1:
            return False
        nums.sort(reverse=True)
        return self.can_partition(nums, summ // 2, 0, {})

    def can_partition(self, nums, target, i, memo):
        if (target, i) in memo:
            return memo[(target, i)]

        if i >= len(nums):
            return False

        if target == 0:
            return True
        if target < 0:
            return False

        # pick or skip
        if self.can_partition(nums, target - nums[i], i + 1, memo) or self.can_partition(nums, target, i + 1, memo):
            return True
        memo[(target, i)] = False
        return False

    # def can_partition(self, nums, target, i, memo, N):
    #     if (target, i) in memo:
    #         return memo[(target, i)]
    #
    #     if target == 0:
    #         return True
    #     if target < 0:
    #         return False
    #
    #     for ii in range(i, len(nums)):
    #         # pick or skip
    #         if self.can_partition(nums, target - nums[ii], ii + 1, memo, N) or self.can_partition(nums, target, ii + 1, memo, N):
    #             return True
    #     memo[(target, i)] = False
    #     return False

    # Tabulation

    # def canPartition(self, nums: List[int]) -> bool:
    #     summ = sum(nums)
    #     if summ & 1:
    #         return False
    #     target = summ // 2
    #     dp = [False] * (target + 1)
    #     dp[0] = True
    #     for s in range(target+1):
    #         for num in nums:
    #
    #
    #
    #
    #     return dp[-1]


if __name__ == '__main__':
    init = PartitionEqualSubsetSum()
    print(init.canPartition([1, 5, 11, 5]))  # True
    print(init.canPartition([1, 2, 3, 5]))  # False
    print(init.canPartition([1, 2, 5]))  # False
    print(init.canPartition([1, 2, 3, 4, 5, 6, 7]))  # True
    print(init.canPartition([14, 9, 8, 4, 3, 2]))  # True
    # print(init.canPartition(
    #     [4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 12, 12, 12, 12, 12, 12, 12, 12, 16, 16, 16, 16, 16, 16, 16, 16, 20, 20, 20, 20, 20, 20, 20,
    #      20, 24, 24, 24, 24, 24, 24, 24, 24, 28, 28, 28, 28, 28, 28, 28, 28, 32, 32, 32, 32, 32, 32, 32, 32, 36, 36, 36, 36, 36, 36, 36, 36, 40, 40,
    #      40, 40, 40, 40, 40, 40, 44, 44, 44, 44, 44, 44, 44, 44, 48, 48, 48, 48, 48, 48, 48, 48, 52, 52, 52, 52, 52, 52, 52, 52, 56, 56, 56, 56, 56,
    #      56, 56, 56, 60, 60, 60, 60, 60, 60, 60, 60, 64, 64, 64, 64, 64, 64, 64, 64, 68, 68, 68, 68, 68, 68, 68, 68, 72, 72, 72, 72, 72, 72, 72, 72,
    #      76, 76, 76, 76, 76, 76, 76, 76, 80, 80, 80, 80, 80, 80, 80, 80, 84, 84, 84, 84, 84, 84, 84, 84, 88, 88, 88, 88, 88, 88, 88, 88, 92, 92, 92,
    #      92, 92, 92, 92, 92, 96, 96, 96, 96, 96, 96, 96, 96, 97, 99]))

    print(init.canPartition(
        [5, 79, 2, 4, 8, 16, 32, 64, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]))
