from typing import *


class TransposeMatrix:
    # def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    #     if not matrix:
    #         return None
    #
    #     R = len(matrix)
    #     C = len(matrix[0])
    #
    #     for r in range(R):
    #         for c in range(r, C):
    #             matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    #     return matrix

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return None

        R = len(matrix)
        C = len(matrix[0])

        new_matrix = [[0] * R for _ in range(C)]
        for r in range(R):
            for c in range(C):
                new_matrix[c][r] = matrix[r][c]
        return new_matrix


if __name__ == '__main__':
    init = TransposeMatrix()
    print(init.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [[1,4,7],[2,5,8],[3,6,9]]
    print(init.transpose(matrix=[[1, 2, 3], [4, 5, 6]]))  # [[1,4],[2,5],[3,6]]
