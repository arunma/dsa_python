from collections import defaultdict
from typing import *

WHITE, GRAY, BLACK = 0, 1, 2


class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        colors = defaultdict(int)
        for u in range(numCourses):
            if self.has_cycle(graph, u, colors):
                return False
        return True

    def has_cycle(self, graph, node, colors):
        colors[node] = GRAY
        for nei in graph[node]:
            if colors[nei] == WHITE:
                if self.has_cycle(graph, nei, colors):
                    return True
            elif colors[nei] == GRAY:
                return True
            else:
                continue
        colors[node] = BLACK
        return False


if __name__ == "__main__":
    init = CourseSchedule()
    print(init.canFinish(2, [[1, 0]]))  # true
    print(init.canFinish(2, [[1, 0], [0, 1]]))  # false
