from typing import *


class FloodFill:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R = len(grid)
        C = len(grid[0])

        sval = grid[sr][sc]
        seen = set()
        self.dfs(grid, sval, sr, sc, R, C, seen, tval=color)

    def dfs(self, grid, sval, r, c, R, C, seen, tval):
        seen.add((r, c))
        grid[r][c] = tval
        neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for nr, nc in neis:
            if -1 < nr < R and -1 < nc < C and grid[nr][nc] == sval and (nr, nc) not in seen:
                self.dfs(grid, sval, nr, nc, R, C, seen, tval)


if __name__ == '__main__':
    init = FloodFill()
    print(init.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))  # [[2,2,2],[2,2,0],[2,0,1]]
    print(init.floodFill([[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0))  # [[0,0,0],[0,1,1]]
