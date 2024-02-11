import heapq
from typing import *
from collections import Counter


class ReorganizeString:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        pq = []
        for k, v in counter.items():
            heapq.heappush(pq, (-v, k))

        prev = []
        result = ""
        while pq:
            count, c = heapq.heappop(pq)
            count *= -1
            if prev:
                heapq.heappush(pq, prev.pop())

            result += c
            if count - 1 > 0:
                prev = [(-(count - 1), c)]

        if len(result) == len(s):
            return result
        return ""

    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        pq = []
        for k, v in counter.items():
            heapq.heappush(pq, (-v, k))

        prev = None
        result = ""
        while pq:
            count, c = heapq.heappop(pq)
            count *= -1
            if prev:
                heapq.heappush(pq, prev)
                prev = None

            result += c
            if count - 1 > 0:
                prev = (-(count - 1), c)

        if len(result) == len(s):
            return result
        return ""


if __name__ == '__main__':
    init = ReorganizeString()
    print(init.reorganizeString("aab"))  # "aba"
    print(init.reorganizeString("aaab"))  # ""
