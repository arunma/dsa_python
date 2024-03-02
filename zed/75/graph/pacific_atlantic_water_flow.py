from collections import deque
from typing import *


class PacificAtlanticWaterFlow:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        R = len(heights)
        C = len(heights[0])
        pstarts = []
        astarts = []
        for r in range(R):
            for c in range(C):
                if r == 0 or c == 0:
                    pstarts.append((r, c))
                if r == R - 1 or c == C - 1:
                    astarts.append((r, c))

        pseen = self.bfs(heights, pstarts, R, C)
        aseen = self.bfs(heights, astarts, R, C)

        # return pseen.intersection(aseen)
        return pseen & aseen

    def bfs(self, heights, starts, R, C):
        queue = deque(starts)
        seen = set(starts)
        while queue:
            (r, c) = queue.popleft()
            neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in neis:
                if -1 < nr < R and -1 < nc < C and heights[nr][nc] >= heights[r][c] and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    queue.append((nr, nc))
        return seen

    # def pacificAtlantic(self, matrix):
    #     if not matrix: return []
    #     m, n = len(matrix), len(matrix[0])
    #
    #     def bfs(reachable_ocean):
    #         q = collections.deque(reachable_ocean)
    #         while q:
    #             (i, j) = q.popleft()
    #             for (di, dj) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #                 if 0 <= di + i < m and 0 <= dj + j < n and (di + i, dj + j) not in reachable_ocean \
    #                         and matrix[di + i][dj + j] >= matrix[i][j]:
    #                     q.append((di + i, dj + j))
    #                     reachable_ocean.add((di + i, dj + j))
    #         return reachable_ocean
    #
    #     pacific = set([(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)])
    #     atlantic = set([(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n - 1)])
    #     print(pacific)
    #     print(atlantic)
    #     return list(bfs(pacific) & bfs(atlantic))


if __name__ == "__main__":
    init = PacificAtlanticWaterFlow()
    print(init.pacificAtlantic([[1]]))  # [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    # print(init.pacificAtlantic(
    #     [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))  # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    # print(init.pacificAtlantic([[2, 1], [1, 2]]))  # [[0,0],[0,1],[1,0],[1,1]]
    # print(init.pacificAtlantic([[1, 1], [1, 1], [1, 1]]))  # [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
