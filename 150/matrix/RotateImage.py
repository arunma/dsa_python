from typing import *


class RotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])

        for r in range(R):
            for c in range(r, C):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for i in range(R):
            self.reverse(matrix, i)

        print(matrix)

    def reverse(self, matrix, row):
        cl = 0
        cr = len(matrix[0]) - 1

        while cl < cr:
            matrix[row][cl], matrix[row][cr] = matrix[row][cr], matrix[row][cl]
            cl += 1
            cr -= 1


if __name__ == '__main__':
    init = RotateImage()
    print(init.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [[7,4,1],[8,5,2],[9,6,3]]
    # print(init.rotate(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # [[9,5,1],[10,6,2],[11,7,3],[12,8,4]]
