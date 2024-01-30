import heapq
from collections import defaultdict
from typing import *


class NetworkDelayTime:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
            # graph[v].append((u, w))

        pq = [(0, k)]
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        while pq:
            cost, node = heapq.heappop(pq)
            print(f"cost: {cost}, node: {node}")

            for nei, nei_cost in graph[node]:
                new_cost = cost + nei_cost
                if dist[nei] > new_cost:
                    dist[nei] = new_cost
                    heapq.heappush(pq, (new_cost, nei))

        max_dist = max(dist[1:])
        print(dist)
        return max_dist if max_dist < float('inf') else -1


if __name__ == '__main__':
    init = NetworkDelayTime()
    # print(init.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))  # 2
    # print(init.networkDelayTime(times=[[1, 2, 1]], n=2, k=2))  # 1
    print(init.networkDelayTime(times=[[1, 2, 2], [1, 4, 6], [2, 4, 7], [2, 3, 5], [4, 3, 8]], n=4, k=1))  # 7
