from collections import defaultdict
from typing import *


class CourseScheduleII:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        colors = defaultdict(int)
        WHITE, GRAY, BLACK = 0, 1, 2
        order = []

        def has_cycle(u):
            colors[u] = GRAY
            for v in graph[u]:
                if colors[v] == GRAY:
                    return True
                elif colors[v] == WHITE and has_cycle(v):
                    return True
                else:
                    continue
            order.append(u)
            colors[u] = BLACK
            return False

        for u in range(numCourses):
            if colors[u] == WHITE and has_cycle(u):
                return None
        return order


if __name__ == '__main__':
    init = CourseScheduleII()
    print(init.findOrder(numCourses=2, prerequisites=[[1, 0]]))  # [0,1]
    print(init.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))  # [0,2,1,3] or [0,1,2,3]
    print(init.findOrder(numCourses=1, prerequisites=[]))  # [0]
