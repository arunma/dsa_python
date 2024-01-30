from typing import *


class NumberOfIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        R = len(grid)
        C = len(grid[0])

        seen = set()
        for r in range(R):
            for c in range(C):
                if (r, c) not in seen and grid[r][c] == '1':
                    seen.add((r, c))
                    self.dfs(r, c, R, C, grid, seen)
                    islands += 1
        return islands

    def dfs(self, r, c, R, C, grid, seen):
        neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for nr, nc in neis:
            if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen and grid[nr][nc] == '1':
                seen.add((nr, nc))
                if self.dfs(nr, nc, R, C, grid, seen):
                    return True
        return False

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid:
    #         return 0
    #     islands = 0
    #     R = len(grid)
    #     C = len(grid[0])
    #
    #     for r in range(R):
    #         for c in range(C):
    #             if grid[r][c] == '1':
    #                 self.dfs(r, c, R, C, grid)
    #                 islands += 1
    #
    #     return islands
    #
    # def dfs(self, r, c, R, C, grid):
    #     grid[r][c] = '0'
    #     neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    #     for nr, nc in neis:
    #         if -1 < nr < R and -1 < nc < C and grid[nr][nc] == '1':
    #             self.dfs(nr, nc, R, C, grid)


if __name__ == '__main__':
    init = NumberOfIslands()
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]
    print(init.numIslands(grid))  # 1

    grid2 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    print(init.numIslands(grid2))  # 3
    print(init.numIslands([]))  # 0
