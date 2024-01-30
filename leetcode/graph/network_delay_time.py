import heapq
from collections import defaultdict
from typing import *


class NetworkDelayTime:
    # dijkstra's
    # Space: O(E)
    # Time: PQ has to store a maximum ofa
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        dist[0] = 0

        pq = [(0, k)]  # dist, src
        while pq:
            curr_dist, node = heapq.heappop(pq)
            for nei, ndist in graph[node]:
                new_dist = curr_dist + ndist
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(pq, (new_dist, nei))

        ret_dist = max(dist)
        return -1 if ret_dist == float('inf') else ret_dist

    # bellman ford - O(VE), O(V)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        dist[0] = 0

        for node in range(1, n + 1):
            for u, v, w in times:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
        ret_dist = max(dist)
        return -1 if ret_dist == float('inf') else ret_dist


if __name__ == '__main__':
    init = NetworkDelayTime()
    print(init.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # 2
    print(init.networkDelayTime([[1, 2, 1]], 2, 1))  # 1
    print(init.networkDelayTime([[1, 2, 1], [2, 1, 3]], 2, 2))  # 3
