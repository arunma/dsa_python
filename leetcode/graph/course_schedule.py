from collections import defaultdict
from typing import *

WHITE, GRAY, BLACK = 0, 1, 2


class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        colors = [0] * numCourses

        for u in range(numCourses):
            if colors[u] == WHITE and self.has_cycle(u, graph, colors):
                return False

        return True

    def has_cycle(self, u, graph, colors):
        colors[u] = GRAY
        for v in graph[u]:
            if colors[v] == GRAY:
                return True
            elif colors[v] == WHITE:
                if self.has_cycle(v, graph, colors):
                    return True
            else:
                continue
        colors[u] = BLACK
        return False


if __name__ == '__main__':
    init = CourseSchedule()
    print(init.canFinish(numCourses=2, prerequisites=[[1, 0]]))  # True
    print(init.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))  # False
    print(init.canFinish(numCourses=3, prerequisites=[[1, 0], [1, 2], [0, 1]]))  # False
