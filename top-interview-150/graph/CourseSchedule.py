from collections import defaultdict
from typing import *


class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses:
            return False

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        colors = defaultdict(int)
        WHITE, GRAY, BLACK = 0, 1, 2

        def has_cycle(u):
            colors[u] = GRAY
            for v in graph[u]:
                if colors[v] == GRAY:
                    return True
                elif colors[v] == WHITE and has_cycle(v):
                    return True
                else:
                    continue
            colors[u] = BLACK
            return False

        for u in range(numCourses):
            if colors[u] == WHITE:
                if has_cycle(u):
                    return False
        return True


if __name__ == '__main__':
    init = CourseSchedule()
    print(init.canFinish(numCourses=2, prerequisites=[[1, 0]]))  # True
    print(init.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))  # False
