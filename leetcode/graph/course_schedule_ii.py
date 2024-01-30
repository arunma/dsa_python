from collections import defaultdict
from typing import *

WHITE, GRAY, BLACK = 0, 1, 2


class CourseScheduleIi:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        colors = [0] * numCourses

        order = []
        for u in range(numCourses):
            if colors[u] == WHITE and self.has_cycle(u, graph, colors, order):
                return []

        return [] if len(order) != numCourses else order

    def has_cycle(self, u, graph, colors, order):
        colors[u] = GRAY
        for v in graph[u]:
            if colors[v] == GRAY:
                return False
            elif colors[v] == WHITE:
                if self.has_cycle(v, graph, colors, order):
                    return False
            else:
                continue
        order.append(u)
        colors[u] = BLACK


if __name__ == '__main__':
    init = CourseScheduleIi()
    print(init.findOrder(numCourses=2, prerequisites=[[1, 0]]))  # [0,1]
    print(init.findOrder(numCourses=2, prerequisites=[[1, 0], [0, 1]]))  # []
    print(init.findOrder(numCourses=3, prerequisites=[[1, 0], [1, 2], [0, 1]]))  # []
    print(init.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))  # [0,2,1,3]
