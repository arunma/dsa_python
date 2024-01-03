from typing import *


class DestinationCity:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = {}
        start_src = ''
        for src, dest in paths:
            start_src = src
            graph[src] = dest

        dest = graph[start_src]
        while dest in graph:
            dest = graph[dest]
        return dest


if __name__ == '__main__':
    init = DestinationCity()
    print(init.destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))  # "Sao Paulo"
    print(init.destCity(paths=[["B", "C"], ["D", "B"], ["C", "A"]]))  # "A"
    print(init.destCity(paths=[["A", "Z"]]))  # "Z"
