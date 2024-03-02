from typing import *


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort(key=lambda it: it[0])

        result = []
        mstart, mend = intervals[0]
        for i, (cstart, cend) in enumerate(intervals[1:]):
            if cstart > mend:
                result.append([mstart, mend])
                mstart, mend = cstart, cend
            elif cend >= mend:
                mstart = min(cstart, mstart)
                mend = max(cend, mend)
        result.append([mstart, mend])
        return result


if __name__ == "__main__":
    init = MergeIntervals()
    print(init.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1, 6], [8, 10], [15, 18]]
    print(init.merge(intervals=[[1, 4], [4, 5]]))  # [[1, 5]]
    print(init.merge(intervals=[[1, 4], [0, 4]]))  # [[0, 4]]
