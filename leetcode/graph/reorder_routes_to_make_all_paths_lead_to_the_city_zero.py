from collections import defaultdict, deque
from typing import *


class ReorderRoutesToMakeAllPathsLeadToTheCityZero:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        queue = deque([0])

        seen = set()
        total_cost = 0
        while queue:
            node = queue.popleft()
            seen.add(node)
            for nei, cost in graph[node]:
                if nei not in seen:
                    queue.append(nei)
                    # print(f"node->nei {node} -> {nei}: {cost}")
                    total_cost += cost
        return total_cost


if __name__ == '__main__':
    init = ReorderRoutesToMakeAllPathsLeadToTheCityZero()
    print(init.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))  # 3
    # print(init.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))  # 2
