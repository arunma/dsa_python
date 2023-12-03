from typing import *


class NumberOfDistinctIslands:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        R = len(grid)
        C = len(grid[0])
        dist = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    curr = []
                    self.dfs(grid, r, c, R, C, curr, (0, 0))
                    dist.add(tuple(curr))
        return len(dist)

    def dfs(self, grid, r, c, R, C, curr, pos):
        if -1 < r < R and -1 < c < C and grid[r][c] == 1:
            grid[r][c] = 0
            curr.append(pos)
            pairs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for rd, cd in pairs:
                self.dfs(grid, r + rd, c + cd, R, C, curr, (pos[0] + rd, pos[1] + cd))


if __name__ == '__main__':
    init = NumberOfDistinctIslands()
    print(init.numDistinctIslands(grid=[[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))  # 1
    print(init.numDistinctIslands(grid=[[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]))  # 3
