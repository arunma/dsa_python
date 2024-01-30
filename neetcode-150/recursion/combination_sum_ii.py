from typing import *


class CombinationSumIi:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
            if i != index and candidates[i] == candidates[i - 1]:
                continue
            self.combination_sum(candidates, target, curr + [candidates[i]], curr_sum + candidates[i], i + 1, result)


if __name__ == '__main__':
    init = CombinationSumIi()
    print(init.combinationSum2([10, 1, 2, 7, 6, 1, 5], target=8))  # [[1,1,6],[1,2,5],[1,7],[2,6]]
    print(init.combinationSum2([2, 5, 2, 1, 2], target=5))  # [[1,2,2],[5]]
    print(init.combinationSum2([2, 3, 6, 7], target=7))  # [[7]]
