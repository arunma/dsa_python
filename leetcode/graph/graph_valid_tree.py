from collections import defaultdict
from typing import *

WHITE, GRAY, BLACK = 0, 1, 2


class GraphValidTree:
    # def validTree(self, n: int, edges: List[List[int]]) -> bool:
    #     graph = defaultdict(list)
    #     for u, v in edges:
    #         graph[u].append(v)
    #         graph[v].append(u)
    #
    #     if len(graph) != n:
    #         return False
    #
    #     colors = defaultdict(int)
    #     # came_from = [-1] * n
    #     for node in range(n):
    #         visited = set()
    #         if self.has_cycle(node, graph, -1, visited):
    #             print("returning false")
    #             return False
    #
    #     return True

    # def has_cycle(self, node, graph, parent, seen):
    #     seen.add(node)
    #     for nei in graph[node]:
    #         if nei not in seen:
    #             if self.has_cycle(nei, graph, parent, seen):
    #                 return True
    #         elif nei in seen and nei != parent:
    #             return True
    #     return False

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        if len(graph) != n:
            return False

        colors = defaultdict(int)
        # came_from = [-1] * n
        if self.has_cycle(0, graph, colors, -1):
            return False
        return True

    def has_cycle(self, node, graph, colors, parent):
        colors[node] = GRAY
        for nei in graph[node]:
            if colors[nei] == WHITE and self.has_cycle(nei, graph, colors, node):
                return True
            elif colors[nei] == GRAY and nei != parent:
                return True
            elif colors[nei] == BLACK:
                continue
        colors[node] = BLACK
        return False


if __name__ == '__main__':
    init = GraphValidTree()
    print(init.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]))  # true
    print(init.validTree(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))  # false
