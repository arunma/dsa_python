from collections import deque
from typing import *


class MinimumGeneticMutation:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        seen = set()

        while queue:
            curr, dist = queue.popleft()
            if curr == endGene:
                return dist

            for nxt in bank:
                if nxt not in seen and self.is_one_step_apart(curr, nxt):
                    seen.add(nxt)
                    queue.append((nxt, dist + 1))

        return -1

    def is_one_step_apart(self, start, end) -> bool:
        dist = 0
        for s, e in zip(start, end):
            if s != e:
                dist += 1
        return dist == 1


if __name__ == '__main__':
    init = MinimumGeneticMutation()
    print(init.minMutation(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTA"]))  # 1
    print(init.minMutation(startGene="AACCGGTT", endGene="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"]))  # 2
    print(init.minMutation(startGene="AAAAACCC", endGene="AACCCCCC", bank=["AAAACCCC", "AAACCCCC", "AACCCCCC"]))  # 3
    print(init.minMutation(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]))  # 4
    print(init.minMutation(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTT", "AACCGGTA", "AACCGGTC"]))  # 1
