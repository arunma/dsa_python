import heapq
from typing import *


# revisit
class SmallestRangeCoveringElementsFromKlists:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        right = 0
        for i, each in enumerate(nums):
            heapq.heappush(pq, (each[0], i, 0))
            right = max(right, each[0])

        result = float('-inf'), float('inf')

        while pq:
            left, lindex, index = heapq.heappop(pq)
            if right - left < result[1] - result[0]:
                result = left, right

            if index + 1 == len(nums[lindex]):
                return [result[0], result[1]]

            next_value = nums[lindex][index + 1]
            right = max(right, next_value)
            heapq.heappush(pq, (next_value, lindex, index + 1))


if __name__ == "__main__":
    init = SmallestRangeCoveringElementsFromKlists()
    print(init.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))  # [20, 24]
    print(init.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))  # [1, 1]
