from typing import *


class SearchA2DMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return 0
        R = len(matrix)
        C = len(matrix[0])
        r = 0
        c = C - 1
        while -1 < r < R and -1 < c < C:
            val = matrix[r][c]
            if val == target:
                return True
            elif val < target:
                r += 1
            else:
                c -= 1
        return False


if __name__ == '__main__':
    init = SearchA2DMatrix()
    print(init.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))  # True
    print(init.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))  # False
    print(init.searchMatrix(matrix=[[]], target=0))  # False
