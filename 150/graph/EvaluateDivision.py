from collections import defaultdict, deque
from typing import *


class EvaluateDivision:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1 / val))

        def bfs(source, target):
            if source not in graph or target not in graph:
                return -1
            queue = deque([(source, 1.0)])
            seen = set()
            while queue:
                node, weight = queue.popleft()
                seen.add(node)
                if node == target:
                    return weight
                for nei, wt in graph[node]:
                    if nei not in seen:
                        queue.append((nei, wt * weight))
            return -1

        result = []
        for u, v in queries:
            result.append(bfs(u, v))
        return result


if __name__ == '__main__':
    init = EvaluateDivision()
    print(init.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                            queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))  # [6.0, 0.5, -1.0, 1.0, -1.0]
    print(init.calcEquation(equations=[["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0],
                            queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))  # [3.75000,0.40000,5.00000,0.20000]
    print(init.calcEquation(equations=[["a", "b"]], values=[0.5],
                            queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))  # [0.50000,2.00000,-1.00000,-1.00000]
    print(init.calcEquation(equations=[["a", "aa"]], values=[9.0], queries=[["aa", "a"], ["aa", "aa"]]))  # [0.11111,-1.00000]
