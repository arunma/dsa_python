from collections import defaultdict
from typing import *

WHITE, GRAY, BLACK = 0, 1, 2


class GraphValidTree:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        if len(graph) != n:
            return False

        # colors = defaultdict(int)
        seen = set()
        if self.has_cycle(graph, 0, -1, seen):
            return False

        if len(seen) != len(graph):
            return False
        return True

    def has_cycle(self, graph, node, parent, seen):
        seen.add(node)
        for nei in graph[node]:
            if nei not in seen:
                if self.has_cycle(graph, nei, node, seen):
                    return True
            elif nei in seen and nei != parent:
                return True
        return False

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        if len(graph) != n:
            return False

        colors = defaultdict(int)
        if self.has_cycle(graph, 0, -1, colors):
            return False

        if len(colors) != len(graph):
            return False
        return True

    def has_cycle(self, graph, node, parent, colors):
        colors[node] = GRAY
        for nei in graph[node]:
            if colors[nei] == WHITE:
                if self.has_cycle(graph, nei, node, colors):
                    return True
            elif colors[nei] == GRAY and nei != parent:
                return True
        colors[node] = BLACK
        return False


if __name__ == "__main__":
    init = GraphValidTree()
    print(init.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # True
    print(init.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))  # False
    print(init.validTree(5, [[0, 1], [1, 2], [3, 4]]))  # False
    print(init.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 4]]))  # True
