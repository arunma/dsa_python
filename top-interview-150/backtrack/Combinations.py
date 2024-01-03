from typing import *


class Combinations:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtrack(n, k, result, 1, [])
        return result

    def backtrack(self, n, k, result, index, curr):
        if len(curr) == k:
            result.append(curr)
            return

        for i in range(index, n + 1):
            self.backtrack(n, k, result, i + 1, curr + [i])


if __name__ == '__main__':
    init = Combinations()
    print(init.combine(n=4, k=2))  # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    print(init.combine(n=1, k=1))  # [[1]]
