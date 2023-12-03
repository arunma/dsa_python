from typing import *


class IslandPerimeter:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        R = len(grid)
        C = len(grid[0])
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    count += 4
                    pairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                    for rr, cc in pairs:
                        if -1 < rr < R and -1 < cc < C and grid[rr][cc] == 1:
                            count -= 1
        return count


if __name__ == '__main__':
    init = IslandPerimeter()
    print(init.islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))  # 16
    print(init.islandPerimeter(grid=[[1]]))  # 4
    print(init.islandPerimeter(grid=[[1, 0]]))  # 4
