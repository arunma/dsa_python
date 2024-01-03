import heapq
from typing import *


class FindKPairsWithSmallestSums:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited = set()
        N1 = len(nums1)
        N2 = len(nums2)
        pq = [(nums1[0] + nums2[0], 0, 0)]
        visited.add((0, 0))

        result = []
        while pq:
            summ, ni1, ni2 = heapq.heappop(pq)
            result.append([nums1[ni1], nums2[ni2]])

            if len(result) == k:
                return result
            if ni1 + 1 < N1 and (ni1 + 1, ni2) not in visited:
                visited.add((ni1 + 1, ni2))
                heapq.heappush(pq, (nums1[ni1 + 1] + nums2[ni2], ni1 + 1, ni2))

            if ni2 + 1 < N2 and (ni1, ni2 + 1) not in visited:
                visited.add((ni1, ni2 + 1))
                heapq.heappush(pq, (nums1[ni1] + nums2[ni2 + 1], ni1, ni2 + 1))
        return result


if __name__ == '__main__':
    init = FindKPairsWithSmallestSums()
    print(init.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))  # [[1,2],[1,4],[1,6]]
    print(init.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))  # [[1,1],[1,1]]
    print(init.kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))  # [[1,3],[2,3]]
    print(init.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=10))  # [[1,1],[1,1],[1,2],[1,2],[2,1],[1,3],[1,3],[2,2],[2,3]]
