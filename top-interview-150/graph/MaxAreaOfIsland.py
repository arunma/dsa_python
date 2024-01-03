from typing import *


class MaxAreaOfIsland:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        R = len(grid)
        C = len(grid[0])

        max_area = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    area = self.dfs(grid, r, c, R, C)
                    max_area = max(max_area, area)
        return max_area

    def dfs(self, grid, r, c, R, C):
        if not -1 < r < R or not -1 < c < C or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        pairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        count = 1
        for rr, cc in pairs:
            count += self.dfs(grid, rr, cc, R, C)

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        R = len(grid)
        C = len(grid[0])

        stack = []
        max_area = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    stack = [(r, c)]
                    grid[r][c] = 0
                    count = 0
                    while stack:
                        r, c = stack.pop()
                        count += 1
                        pairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                        for rr, cc in pairs:
                            if -1 < rr < R and -1 < cc < C and grid[rr][cc] == 1:
                                stack.append((rr, cc))
                                grid[rr][cc] = 0
                    max_area = max(max_area, count)
        return max_area


if __name__ == '__main__':
    init = MaxAreaOfIsland()
    # print(init.maxAreaOfIsland(
    #     grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #           [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    #           [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))  # 6
    # print(init.maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]]))  # 0
    print(init.maxAreaOfIsland(grid=[[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))  # 4
