from typing import *


class InsertInterval:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        intervals.sort(key=lambda x: x[0])

        result = []
        nstart, nend = newInterval

        for i, (cstart, cend) in enumerate(intervals):
            # before
            if nstart > cend:
                result.append([cstart, cend])
            # after
            elif cstart > nend:
                result.append([nstart, nend])
                result.extend(intervals[i:])
                return result
            # overlap
            else:
                nstart = min(cstart, nstart)
                nend = max(cend, nend)
        result.append([nstart, nend])
        return result


if __name__ == '__main__':
    init = InsertInterval()
    print(init.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))  # [[1,5],[6,9]]
    print(init.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))  # [[1,2],[3,10],[12,16]]
