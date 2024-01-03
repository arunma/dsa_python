from typing import *


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[0])
        result = []
        mstart = intervals[0][0]
        mend = intervals[0][1]

        for interval in intervals:
            cstart, cend = interval

            if cstart <= mend:
                mend = max(cend, mend)
            else:
                result.append([mstart, mend])
                mstart = cstart
                mend = cend
        # last
        result.append([mstart, mend])
        return result

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[0])
        result = []
        mstart = intervals[0][0]
        mend = intervals[0][1]

        for cstart, cend in intervals:
            if cstart > mend:
                result.append([mstart, mend])
                mstart = cstart
                mend = cend
            else:
                mstart = min(mstart, cstart)
                mend = max(mend, cend)

        result.append([mstart, mend])
        return result


if __name__ == '__main__':
    init = MergeIntervals()
    print(init.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
    print(init.merge(intervals=[[1, 4], [4, 5]]))  # [[1,5]]
    print(init.merge(intervals=[[1, 4], [0, 4]]))  # [[0,4]]
