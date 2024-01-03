from typing import *


class SpiralMatrix:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        re = len(matrix) - 1
        ce = len(matrix[0]) - 1

        rb = 0
        cb = 0

        result = []
        while rb <= re and cb <= ce:
            # left to right
            for ci in range(cb, ce + 1):
                result.append(matrix[rb][ci])
            rb += 1

            # top to bottom
            for ri in range(rb, re + 1):
                result.append(matrix[ri][ce])
            ce -= 1

            # right to left
            if rb <= re:
                for ci in reversed(range(cb, ce + 1)):
                    result.append(matrix[re][ci])
                re -= 1

            # bottom to top
            if cb <= ce:
                for ri in reversed(range(rb, re + 1)):
                    result.append(matrix[ri][cb])
                cb += 1

        return result


if __name__ == '__main__':
    init = SpiralMatrix()
    # print(init.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,3,6,9,8,7,4,5]
    # print(init.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # [1,2,3,4,8,12,11,10,9,5,6,7]
    print(init.spiralOrder(matrix=[[1, 2, 3, 4, 5, 6], [14, 15, 16, 17, 18, 7], [13, 12, 11, 10, 9, 8]]))
