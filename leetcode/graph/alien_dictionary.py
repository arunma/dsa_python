from collections import defaultdict
from typing import *

WHITE, GRAY, BLACK = 0, 1, 2


class AlienDictionary:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)

        # for i in range(len(words) - 1):
        #     word1, word2 = words[i], words[i + 1]
        #     length = min(len(word1), len(word2))
        #     for ii in range(length):
        #         c1 = word1[ii]
        #         c2 = word2[ii]
        #         if c1 != c2:
        #             graph[c1].append(c2)
        #             break

        for word1, word2 in zip(words, words[1:]):
            if word1 != word2 and word1[:len(word2)] == word2:
                return ""
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    graph[c1].append(c2)
                    break
        result = []

        all_chars = [c for word in words for c in word]

        colors = defaultdict(int)
        for c in set(all_chars):
            if colors[c] == WHITE:
                if self.has_cycle(c, colors, graph, result):
                    return ""

        return ''.join(reversed(result))

    def has_cycle(self, c, colors, graph, result):
        colors[c] = GRAY
        for nei in graph[c]:
            if colors[nei] == GRAY:
                return True
            elif colors[nei] == WHITE:
                if self.has_cycle(nei, colors, graph, result):
                    return True
            elif colors[nei] == BLACK:
                continue
        result.append(c)
        colors[c] = BLACK
        return False


if __name__ == '__main__':
    init = AlienDictionary()
    # print(init.alienOrder([
    #     "wrt",
    #     "wrf",
    #     "er",
    #     "ett",
    #     "rftt"
    # ]))  # wertf

    print(init.alienOrder(["abc", "ab"]))  # ""
    # print(init.alienOrder([
    #     "z",
    #     "z"
    # ]))  # zx
    # print(init.alienOrder([
    #     "z",
    #     "x"
    # ]))  # zx
    # print(init.alienOrder(["zy", "zx"]))  # yxz
    #
    # print(init.alienOrder([
    #     "z",
    #     "x",
    #     "z"
    # ]))  # ""
