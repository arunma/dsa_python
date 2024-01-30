import heapq
from collections import defaultdict


class Dijkstra:
    def find_shortest(self, conn, n):
        graph = defaultdict(list)
        for u, v, w in conn:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0.0, 0)]  # cost, src
        seen = set()

        while pq:
            curr_cost, src = heapq.heappop(pq)
            seen.add(src)
            for nei, ncost in graph[src]:
                if nei in seen:
                    continue
                new_cost = curr_cost + ncost
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    heapq.heappush(pq, (dist[nei], nei))
        print(dist)


if __name__ == '__main__':
    init = Dijkstra()
    conn = [
        [0, 1, 3],
        [0, 2, 2],
        [1, 2, 8],
        [1, 5, 2],
        [2, 4, 7],
        [3, 1, 9],
        [3, 5, 1],
        [5, 7, 1],
        [6, 2, 6],
        [6, 4, 7],
        [7, 5, 7],
        [7, 6, 2],
    ]
    print(init.find_shortest(conn, 8))  # [0, 3, 2, 9, 9, 5, 8, 6]
