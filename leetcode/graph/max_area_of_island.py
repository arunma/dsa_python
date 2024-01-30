from typing import *


class MaxAreaOfIsland:
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     R = len(grid)
    #     C = len(grid[0])
    #
    #     max_area = float('-inf')
    #     for r in range(R):
    #         for c in range(C):
    #             ivisit = set()
    #             if grid[r][c] == 1:
    #                 self.dfs(r, c, R, C, grid, ivisit)
    #                 max_area = max(max_area, len(ivisit))
    #
    #     return max_area
    #
    # def dfs(self, r, c, R, C, grid, ivisit):
    #     grid[r][c] = 0
    #     ivisit.add((r, c))
    #     neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    #     for nr, nc in neis:
    #         if -1 < nr < R and -1 < nc < C and grid[nr][nc] == 1:
    #             self.dfs(nr, nc, R, C, grid, ivisit)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        max_area = float('-inf')
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    count = self.dfs(r, c, R, C, grid)
                    max_area = max(max_area, count)

        return max_area if max_area > float('-inf') else 0

    def dfs(self, r, c, R, C, grid):
        grid[r][c] = 0
        neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        count = 1
        for nr, nc in neis:
            if -1 < nr < R and -1 < nc < C and grid[nr][nc] == 1:
                count += self.dfs(nr, nc, R, C, grid)
        return count


if __name__ == '__main__':
    init = MaxAreaOfIsland()
    print(init.maxAreaOfIsland(
        grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))  # 6
    # print(init.maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]]))  # 0
