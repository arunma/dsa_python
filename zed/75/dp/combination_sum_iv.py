from typing import *


class CombinationSumIv:
    # def combinationSum4(self, nums: List[int], target: int) -> int:
    #     return self.combinations_sum(nums, target, 0, [])
    #
    # def combinations_sum(self, nums, target, curr, currl):
    #     if curr == target:
    #         return 1
    #     if curr > target:
    #         return 0
    #
    #     combi = 0
    #     for i in range(len(nums)):
    #         combi += self.combinations_sum(nums, target, curr + nums[i], currl + [nums[i]])
    #     return combi

    # def combinationSum4(self, nums: List[int], target: int) -> int:
    #     memo = {}
    #     return self.combinations_sum(nums, target, memo)
    #
    # def combinations_sum(self, nums, target, memo):
    #     if target == 0:
    #         return 1
    #     if target < 0:
    #         return 0
    #
    #     if target in memo:
    #         return memo[target]
    #
    #     count = 0
    #     for num in nums:
    #         if target >= num:
    #             # print(f"target: {target}, num: {num}")
    #             count += self.combinations_sum(nums, target - num, memo)
    #     memo[target] = count
    #     return count

    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        return self.combinations_sum(nums, target, memo)

    def combinations_sum(self, nums, target, memo):
        if target in memo:
            return memo[target]
        if target == 0:
            return 1
        if target < 0:
            return 0

        count = 0
        for num in nums:
            if target >= num:
                count += self.combinations_sum(nums, target - num, memo)
        memo[target] = count
        return count


if __name__ == "__main__":
    init = CombinationSumIv()
    # print(init.combinationSum4([1, 2, 3], 4))  # 7
    print(init.combinationSum4([9], 3))  # 0
    # print(init.combinationSum4([4, 2, 1], 32))  # 0
