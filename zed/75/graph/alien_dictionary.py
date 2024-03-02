from collections import defaultdict
from typing import *

WHITE, GRAY, BLACK = 0, 1, 2


class AlienDictionary:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        for w1, w2 in zip(words, words[1:]):
            if w1 != w2 and w1[:len(w2)] == w2:
                return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    graph[c1].append(c2)
                    break
        all_chars = set([c for word in words for c in word])

        result = []
        colors = defaultdict(int)
        for c in all_chars:
            if colors[c] == WHITE:
                if self.top_sort(graph, c, result, colors):
                    return ""

        return ''.join(result[::-1])

    def top_sort(self, graph, c, result, colors):
        colors[c] = GRAY
        for nei in graph[c]:
            if colors[nei] == WHITE:
                if self.top_sort(graph, nei, result, colors):
                    return True
            elif colors[nei] == GRAY:
                return True
            else:
                continue
        result.append(c)
        colors[c] = BLACK
        return False


if __name__ == "__main__":
    init = AlienDictionary()
    print(init.alienOrder(words=["wrt", "wrf", "er", "ett", "rftt"]))  # wertf
    print(init.alienOrder(words=["z", "x"]))  # zx
    print(init.alienOrder(words=["z", "x", "z"]))  # ""
    print(init.alienOrder(words=["abc", "ab"]))  # ""
