import heapq
from collections import Counter
from typing import *


class ReorganizeString:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        pq = [(-count, c) for c, count in counter.items()]
        heapq.heapify(pq)

        r = ""
        temp = []

        while pq:
            count, c = heapq.heappop(pq)
            r += c

            while temp:
                ccount, cc = temp.pop()
                heapq.heappush(pq, (ccount, cc))

            count += 1
            if count <= -1:
                temp.append((count, c))

        print(r)
        return r if len(r) == len(s) else ''


if __name__ == '__main__':
    init = ReorganizeString()
    # print(init.reorganizeString(s="aab"))  # "aba"
    # print(init.reorganizeString(s="aaab"))  # ""
    print(init.reorganizeString("vvvlo"))  # "vlvov"
