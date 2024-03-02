from collections import defaultdict
from typing import *


class NumberOfConnectedComponentsInAnUndirectedGraph:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        count = 0
        for node in range(n):
            if node not in seen:
                self.dfs(graph, node, seen)
                count += 1
        return count

    def dfs(self, graph, node, seen):
        seen.add(node)
        for nei in graph[node]:
            if nei not in seen:
                self.dfs(graph, nei, seen)


if __name__ == "__main__":
    init = NumberOfConnectedComponentsInAnUndirectedGraph()
    print(init.countComponents(5, [[0, 1], [1, 2], [3, 4]]))  # 2
    print(init.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))  # 1
    print(init.countComponents(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # 1
