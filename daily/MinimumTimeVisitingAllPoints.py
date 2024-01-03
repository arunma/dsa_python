from typing import *


class MinimumTimeVisitingAllPoints:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        x1, y1 = points[0]
        result = 0
        for i in range(1, len(points)):
            x2, y2 = points[i]
            result += max(abs(x1 - x2), abs(y1 - y2))
            x1, y1 = x2, y2
        return result


if __name__ == '__main__':
    init = MinimumTimeVisitingAllPoints()
    print(init.minTimeToVisitAllPoints(points=[[1, 1], [3, 4], [-1, 0]]))  # 7
    print(init.minTimeToVisitAllPoints(points=[[3, 2], [-2, 2]]))  # 5
