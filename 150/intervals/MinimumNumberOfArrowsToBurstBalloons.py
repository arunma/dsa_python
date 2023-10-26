from typing import *


class MinimumNumberOfArrowsToBurstBalloons:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[0])

        arrows = 0
        ms, me = points[0]
        for xs, xe in points:
            if xs > me:
                arrows += 1
                ms = xs
                me = xe
            elif ms <= xs <= me and ms <= xe <= me:
                ms = max(xs, ms)
                me = min(xe, me)
        arrows += 1
        return arrows


if __name__ == '__main__':
    init = MinimumNumberOfArrowsToBurstBalloons()
    print(init.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))  # 2
    print(init.findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]))  # 4
    print(init.findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]))  # 2
