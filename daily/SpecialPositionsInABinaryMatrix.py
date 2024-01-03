from typing import *


class SpecialPositionsInABinaryMatrix:
    def numSpecial(self, mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat[0])
        rempties = set()
        cempties = set()
        for r in range(R):
            if sum(mat[r]) == 1:
                rempties.add(r)

        for i, c in enumerate(zip(*mat)):
            if sum(c) == 1:
                cempties.add(i)

        result = 0
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 1 and r in rempties and c in cempties:
                    result += 1
        return result


if __name__ == '__main__':
    init = SpecialPositionsInABinaryMatrix()
    print(init.numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]]))  # 1
    print(init.numSpecial(mat=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # 3
    print(init.numSpecial(mat=[[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))  # 2
    print(init.numSpecial(mat=[[0, 0, 0, 0, 0], [1, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                               [0, 0, 0, 1, 1]]))  # 3
