from typing import *


class Subsets:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.subsets_inner(nums, 0, [], result)
        return result

    def subsets_inner(self, nums, index, curr, result):
        if index == len(nums):
            result.append(curr)
            return

        self.subsets_inner(nums, index + 1, curr, result)
        self.subsets_inner(nums, index + 1, curr + [nums[index]], result)


if __name__ == '__main__':
    init = Subsets()
    print(init.subsets([1, 2, 3]))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
