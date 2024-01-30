import heapq
from collections import defaultdict
from typing import *


class PathWithMaximumProbability:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        probs = [float('-inf')] * n
        pq = [(-1.0, start_node)]
        seen = set()

        while pq:
            curr_prob, src = heapq.heappop(pq)
            if src == end_node:
                return -curr_prob
            seen.add(src)
            for nei, nei_prob in graph[src]:
                if nei in seen:
                    continue
                new_prob = abs(-curr_prob * nei_prob)
                if new_prob > probs[nei]:
                    probs[nei] = new_prob
                    heapq.heappush(pq, (-new_prob, nei))
        return 0


if __name__ == '__main__':
    init = PathWithMaximumProbability()
    print(init.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start_node=0, end_node=2))  # 0.25
    print(init.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start_node=0, end_node=2))  # 0.3
    print(init.maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start_node=0, end_node=2))  # 0.0
    print(init.maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start_node=0, end_node=1))  # 0.5
    print(
        init.maxProbability(n=5, edges=[[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]], succProb=[0.37, 0.17, 0.93, 0.23, 0.39, 0.04], start_node=3,
                            end_node=4))  # 0.2139
