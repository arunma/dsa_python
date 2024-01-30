from typing import *


class IsGraphBipartite:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        colors = {}
        for u in range(N):
            if u not in colors:
                colors[u] = 1
                if not self.is_two_colorable(u, graph, colors):
                    return False
        return True

    def is_two_colorable(self, u, graph, colors):
        for v in graph[u]:
            if v not in colors:
                colors[v] = -colors[u]
                if not self.is_two_colorable(v, graph, colors):
                    return False
            elif colors[v] == -colors[u]:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    init = IsGraphBipartite()
    print(init.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))  # True
    print(init.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))  # False
    print(init.isBipartite([[1], [0, 3], [3], [1, 2]]))  # true
