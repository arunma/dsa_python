from typing import *


class Findmissingandrepeatedvalues:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        array = []
        for r in range(N):
            for c in range(N):
                array.append(grid[r][c])
        array.sort()
        repeat = -1
        missing = -1
        # find missing and repeated
        for i in range(len(array)):
            # handle first element
            if i == 0 and array[i] != 1:
                missing = 1
            if array[i] == array[i - 1]:
                repeat = array[i]
            elif array[i] - array[i - 1] > 1:
                missing = array[i - 1] + 1
        if missing == -1:
            missing = N * N
        return [repeat, missing]


if __name__ == '__main__':
    init = Findmissingandrepeatedvalues()
    print(init.findMissingAndRepeatedValues(grid=[[1, 3], [2, 2]]))
    print(init.findMissingAndRepeatedValues(grid=[[2, 2], [3, 4]]))
    print(init.findMissingAndRepeatedValues(grid=[[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
