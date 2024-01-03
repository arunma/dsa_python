from collections import deque
from typing import *


class ShortestPathInBinaryMatrix:
    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     R = len(grid)
    #     C = len(grid[0])
    #
    #     seen = set()
    #
    #     if grid[0][0] == 0:
    #         res, curr = self.backtrack(grid, 0, 0, R, C, seen, 0)
    #         if res:
    #             return curr
    #     return -1
    #
    # def backtrack(self, grid, r, c, R, C, seen, curr):
    #     if r == R - 1 and c == C - 1:
    #         return curr
    #     seen.add((r, c))
    #     neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c + 1), (r + 1, c - 1)]
    #     for nr, nc in neis:
    #         min_curr = float('inf')
    #         if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen and grid[nr][nc] == 0:
    #             min_curr = min(min_curr, self.backtrack(grid, nr, nc, R, C, seen, curr + 1))
    #     seen.remove((r, c))
    #     return -1

    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     R = len(grid)
    #     C = len(grid[0])
    #
    #     if grid[0][0] != 0:
    #         return -1
    #     queue = deque([(0, 0, 1, [])])
    #     seen = set()
    #
    #     while queue:
    #         r, c, l, curr = queue.popleft()
    #         if (r, c) == (R - 1, C - 1):
    #             return l
    #         seen.add((r, c))
    #         neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c + 1), (r + 1, c - 1)]
    #         for nr, nc in neis:
    #             if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen and grid[nr][nc] == 0:
    #                 queue.append((nr, nc, l + 1, curr + [(nr, nc)]))
    #     return -1

    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     R = len(grid)
    #     C = len(grid[0])
    #
    #     if grid[0][0] != 0:
    #         return -1
    #     queue = deque([(0, 0, 1)])
    #     seen = set()
    #     seen.add((0, 0))
    #
    #     while queue:
    #         r, c, l = queue.popleft()
    #         if (r, c) == (R - 1, C - 1):
    #             return l
    #
    #         neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c + 1), (r + 1, c - 1)]
    #         for nr, nc in neis:
    #             if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen and grid[nr][nc] == 0:
    #                 seen.add((r, c))
    #                 queue.append((nr, nc, l + 1))
    #     return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        if grid[0][0] != 0:
            return -1

        grid[0][0] = 1
        queue = deque([(0, 0, 1)])
        while queue:
            r, c, l = queue.popleft()
            if (r, c) == (R - 1, C - 1):
                return l

            neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c + 1), (r + 1, c - 1)]
            for nr, nc in neis:
                if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen and grid[nr][nc] == 0:
                    seen.add((r, c))
                    queue.append((nr, nc, l + 1))
        return -1


if __name__ == '__main__':
    init = ShortestPathInBinaryMatrix()
    print(init.shortestPathBinaryMatrix(grid=[[0, 1], [1, 0]]))  # 2
    print(init.shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]]))  # 4
    print(init.shortestPathBinaryMatrix(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]]))  # -1
