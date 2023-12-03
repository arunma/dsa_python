from typing import *


class NumberOfIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        R = len(grid)
        C = len(grid[0])

        num_islands = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c, R, C)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, r, c, R, C):
        if not -1 < r < R or not -1 < c < C or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        pairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for rr, cc in pairs:
            self.dfs(grid, rr, cc, R, C)


if __name__ == '__main__':
    init = NumberOfIslands()
    print(init.numIslands(grid=[["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))  # 1
    print(init.numIslands(grid=[["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))  # 3
