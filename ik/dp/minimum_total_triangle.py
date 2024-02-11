from typing import List


class MinimumTotalTriangle:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                triangle[r][c] += min(triangle[r + 1][c], triangle[r + 1][c + 1])
        return triangle[0][0]


if __name__ == '__main__':
    init = MinimumTotalTriangle()
    print(init.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # 11
    print(init.minimumTotal(triangle=[[-10]]))  # -10
