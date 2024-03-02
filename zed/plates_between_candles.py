import bisect
from collections import defaultdict
from typing import *


class PlatesBetweenCandles:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [0]
        candles = []
        for i, c in enumerate(s):
            if c == '|':
                prefix.append(prefix[-1])
                candles.append(i)
            else:
                prefix.append(prefix[-1] + 1)
        result = []
        for start, end in queries:
            # low = bisect.bisect_left(candles, start)
            low = self.bin_search_left(candles, start, 0, len(candles) - 1)
            # high = bisect.bisect_right(candles, end) - 1
            high = self.bin_search_right(candles, end, 0, len(candles) - 1) - 1
            if high >= 0 and low < len(candles) and low <= high:
                result.append(prefix[candles[high] + 1] - prefix[candles[low] + 1])
            else:
                result.append(0)

        return result

    def bin_search_left(self, arr, target, low, high):
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low += 1
            else:
                high -= 1
        return low

    def bin_search_right(self, arr, target, low, high):
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= target:
                low += 1
            else:
                high -= 1
        return low

    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        candles = []
        prev = 0
        plates = []
        # for i, c in enumerate(s):
        #     if c == '|':
        #         plates.append(plates[-1])
        #         candles.append(i)
        #     else:
        #         plates.append(plates[-1] + 1)
        # print(plates)
        for i, c in enumerate(s):
            if c == '|':
                plates.append(prev)
                candles.append(i)
            else:
                plates.append(prev + 1)
                prev = plates[-1]

        # print("candles: ", candles)
        # print("plates: ", plates)
        result = []
        for l, r in queries:
            left = bisect.bisect_left(candles, l)
            right = bisect.bisect_right(candles, r) - 1

            # if left < 0 or right > len(candles) or right < left:
            if right < left:
                result.append(0)
            else:
                candle_count = plates[candles[right]] - plates[candles[left]]
                result.append(candle_count)
        return result


if __name__ == "__main__":
    init = PlatesBetweenCandles()
    print(init.platesBetweenCandles(s="**|**|***|", queries=[[2, 5], [5, 9]]))  # [2, 3]
    print(init.platesBetweenCandles(s="**|**|***|", queries=[[5, 9]]))  # [2, 3]
    print(init.platesBetweenCandles(s="***|**|*****|**||**|*", queries=[[4, 5]]))  # [0]
    print(init.platesBetweenCandles(s="***|**|*****|**||**|*", queries=[[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))  # [9, 0, 0, 0, 0]
