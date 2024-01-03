from collections import Counter
from typing import *


class TopKFrequentElements:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counter = Counter(nums)
    #
    #     pq = []
    #     for num, count in counter.items():
    #         if len(pq) < k:
    #             heapq.heappush(pq, (count, num))
    #         else:
    #             heapq.heappushpop(pq, (count, num))
    #
    #     result = []
    #     for _ in range(k):
    #         count, num = heapq.heappop(pq)
    #         result.append(num)
    #     return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        N = len(nums)
        bucket = [[] for _ in range(N + 1)]
        for num, count in counter.items():
            bucket[count].append(num)
        # result = []
        # for lst in reversed(bucket):
        #     for key in lst:
        #         result.append(key)
        #         if len(result) == k:
        #             return result
        flat = [key for lst in bucket for key in lst]
        return flat[::-1][:k]
        # return []


if __name__ == '__main__':
    init = TopKFrequentElements()
    # print(init.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))  # [1, 2]
    #    print(init.topKFrequent(nums=[1], k=1))  # [1]
    print(init.topKFrequent(nums=[3, 0, 1, 0], k=1))  # [1]
