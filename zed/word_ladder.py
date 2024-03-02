from collections import defaultdict, deque
from typing import *


class WordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList = set(wordList)

        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                graph[key].append(word)

        queue = deque([(beginWord, 1)])
        seen = set()
        while queue:
            curr, dist = queue.popleft()
            seen.add(curr)
            if curr == endWord:
                return dist

            for i in range(len(curr)):
                key = curr[:i] + "*" + curr[i + 1:]
                for nei in graph[key]:
                    if nei not in seen:
                        queue.append((nei, dist + 1))
        return 0


if __name__ == "__main__":
    init = WordLadder()
    print(init.ladderLength("hot", "dog", ["hot", "dog"]))  # 2
    print(init.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
    print(init.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
    print(init.ladderLength("a", "c", ["a", "b", "c"]))  # 2
