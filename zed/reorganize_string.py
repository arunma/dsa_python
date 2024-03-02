import heapq
from collections import Counter


class ReorganizeString:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)

        pq = []
        for c, count in counter.items():
            heapq.heappush(pq, (-count, c))

        temp = []

        result = ""
        while pq:
            (rev_count, c) = heapq.heappop(pq)
            act_count = -rev_count

            while temp:
                ac, cc = temp.pop()
                heapq.heappush(pq, (-ac, cc))

            result += c
            if act_count - 1 > 0:
                temp.append((act_count - 1, c))

        return result if len(result) == len(s) else ""


if __name__ == "__main__":
    init = ReorganizeString()
    print(init.reorganizeString(s="aab"))  # "aba"
    print(init.reorganizeString(s="aaab"))  # ""
    print(init.reorganizeString("vvvlo"))  # "vlvov"
