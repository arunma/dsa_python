import heapq
from collections import deque
from typing import *


class SlidingWindowMaximum:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []

        result = []
        for we, num in enumerate(nums):
            heapq.heappush(pq, (-num, we))
            if we + 1 >= k:
                while pq and pq[0][1] <= we - k:
                    heapq.heappop(pq)
                result.append(-pq[0][0])
        return result

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        queue = deque([0])
        for we, num in enumerate(nums):
            if queue and queue[0] <= (we - k):
                queue.popleft()

            while queue and num >= nums[queue[-1]]:
                queue.pop()
            queue.append(we)

            result.append(nums[queue[0]])
        return result

    def push_to_deque(self, queue, num, i):
        while queue and num >= queue[0]:
            queue.popleft()
        queue.append(num)


if __name__ == '__main__':
    init = SlidingWindowMaximum()
    print(init.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))  # [3,3,5,5,6,7]
    # print(init.maxSlidingWindow(nums=[1], k=1))  # [1]
    # print(init.maxSlidingWindow([9, 10, 9, -7, -4, -8, 2, -6], 5))  # [10,10,9,2]
    # print(init.maxSlidingWindow([8, 7, 6, 9], 2))
