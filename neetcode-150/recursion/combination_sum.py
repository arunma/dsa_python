from typing import *


class CombinationSum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.combination_sum(candidates, target, [], 0, 0, result)
        return result

    def combination_sum(self, candidates, target, curr, curr_sum, index, result):
        if curr_sum < 0 or curr_sum > target:
            return

        if curr_sum == target:
            result.append(curr.copy())
            return

        for i in range(index, len(candidates)):
            self.combination_sum(candidates, target, curr + [candidates[i]], curr_sum + candidates[i], i, result)


if __name__ == '__main__':
    init = CombinationSum()
    print(init.combinationSum([2, 3, 6, 7], target=7))  # [[2,2,3],[7]]
    print(init.combinationSum([2, 3, 5], target=8))  # [[2,2,2,2],[2,3,3],[3,5]]
    print(init.combinationSum([2], target=1))  # []
