from typing import *


class InsertInterval:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        intervals.sort(key=lambda i: i[0])

        result = []
        mstart, mend = newInterval
        for i, cint in enumerate(intervals):
            cstart, cend = cint

            if cend < mstart:
                result.append(cint)
            elif cstart > mend:
                result.append([mstart, mend])
                result.extend(intervals[i:])
                return result
            else:
                mstart = min(cstart, mstart)
                mend = max(cend, mend)
        result.append([mstart, mend])
        return result


if __name__ == "__main__":
    init = InsertInterval()
    # print(init.insert([[1, 3], [6, 9]], [2, 5]))  # [[1, 5], [6, 9]]
    print(init.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # [[1, 2], [3, 10], [12, 16]]
    print(init.insert([], [5, 7]))  # [[5, 7]]
    print(init.insert([[1, 5]], [2, 3]))  # [[1, 5]]
