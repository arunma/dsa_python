import heapq
from typing import *


class PathWithMinimumEffort:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R = len(heights)
        C = len(heights[0])

        pq = [(0.0, 0, 0,)]
        dist = [[float('inf') for _ in range(C)] for _ in range(R)]
        dist[0][0] = 0
        seen = set()
        while pq:
            eff, r, c = heapq.heappop(pq)
            seen.add((r, c))
            if (r, c) == (R - 1, C - 1):
                return eff

            nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in nei:
                if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen:
                    new_eff = max(eff, abs(heights[r][c] - heights[nr][nc]))
                    dist[nr][nc] = new_eff
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))
        return -1


if __name__ == '__main__':
    init = PathWithMinimumEffort()
    print(init.minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))  # 2
    print(init.minimumEffortPath(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]]))  # 1
    print(init.minimumEffortPath(heights=[[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1],
                                          [1, 1, 1, 2, 1]]))  # 0
