from typing import *


class Permutations:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        self.backtrack(nums, result, used, [])
        return result

    def backtrack(self, nums, result, used, curr):
        if len(curr) == len(nums):
            result.append(curr)
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            self.backtrack(nums, result, used, curr + [nums[i]])
            used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, result, [])
        return result

    def backtrack(self, nums, result, curr):
        if not nums:
            result.append(curr.copy())
            return

        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i + 1:], result, curr + [nums[i]])


if __name__ == '__main__':
    init = Permutations()
    print(init.permute(nums=[1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(init.permute(nums=[0, 1]))  # [[0, 1], [1, 0]]
    print(init.permute(nums=[1]))  # [[1]]
