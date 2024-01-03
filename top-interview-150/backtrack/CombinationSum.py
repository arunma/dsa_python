from typing import *


class CombinationSum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(candidates, target, result, [], 0)
        return result

    def backtrack(self, candidates, target, result, curr, index):
        if target == 0:
            result.append(curr.copy())
            return
        if target < 0:
            return

        for i in range(index, len(candidates)):
            self.backtrack(candidates, target - candidates[i], result, curr + [candidates[i]], i)


if __name__ == '__main__':
    init = CombinationSum()
    print(init.combinationSum([2, 3, 6, 7], target=7))  # [[2,2,3],[7]]
    print(init.combinationSum([2, 3, 5], target=8))  # [[2,2,2,2],[2,3,3],[3,5]]
    print(init.combinationSum([2], target=1))  # []
