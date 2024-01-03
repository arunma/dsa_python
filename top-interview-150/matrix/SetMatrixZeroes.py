from typing import *


class SetMatrixZeroes:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])
        zr = []
        zc = []

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    zr.append(r)
                    zc.append(c)

        for r in range(R):
            for c in range(C):
                if r in zr or c in zc:
                    matrix[r][c] = 0

        print(matrix)

    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_has_zero = True

                    if c == 0:
                        first_col_has_zero = True

                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, R):
            for c in range(1, C):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_has_zero:
            for c in range(C):
                matrix[0][c] = 0

        if first_col_has_zero:
            for r in range(R):
                matrix[r][0] = 0

        print(matrix)


if __name__ == '__main__':
    init = SetMatrixZeroes()
    # print(init.setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print(init.setZeroes(matrix=[[1, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))  # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
