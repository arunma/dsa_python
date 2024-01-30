import heapq
import io
import sys
from collections import defaultdict, deque


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def connect(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_all_distances(self, s):
        dist = [float('inf')] * self.n
        dist[s] = 0
        pq = [(0, 0)]
        while pq:
            curr_cost, curr = heapq.heappop(pq)
            for nei, nei_cost in self.graph[curr]:
                new_cost = curr_cost + nei_cost
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    heapq.heappush(pq, (new_cost, curr))

        result = [d if d < float('inf') else -1 for d in dist[1:]]
        print(result)

    def __str__(self):
        return self.graph.__str__()

    # bfs
    def find_all_distances(self, s):
        queue = deque([])
        queue.append((s, 0))
        dist = [-1] * (self.n + 1)
        seen = set()
        while queue:
            node, cost = queue.popleft()
            seen.add(node)
            dist[node] = cost
            for nei in self.graph[node]:
                if nei not in seen:
                    queue.append((nei, cost + 6))

        del dist[s]
        result = [str(d) for d in dist[1:]]

        print(" ".join(result))


if __name__ == '__main__':

    sys.stdin = io.StringIO("""2
    4 2
    1 2
    1 3
    1
    3 1
    2 3
    2""")

    #     sys.stdin = io.StringIO("""1
    # 7 4
    # 1 2
    # 1 3
    # 3 4
    # 2 5
    # 2""")
    t = int(input())
    for i in range(t):
        n, m = [int(value) for value in input().split()]
        graph = Graph(n)
        for i in range(m):
            x, y = [int(x) for x in input().split()]
            graph.connect(x, y)
        s = int(input())
        graph.find_all_distances(s)  # 6 12 18 6 -1 -1
