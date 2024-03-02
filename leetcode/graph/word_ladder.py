from collections import defaultdict, deque
from typing import *


class Word_ladder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                graph[key].append(word)

        seen = set()
        queue = deque([(beginWord, 1)])
        while queue:
            curr, cnt = queue.popleft()
            seen.add(curr)
            if curr == endWord:
                return cnt

            for i in range(len(curr)):
                key = curr[:i] + '*' + curr[i + 1:]
                for nei in graph[key]:
                    if nei not in seen:
                        queue.append((nei, cnt + 1))

        return 0


if __name__ == "__main__":
    init = Word_ladder()
    print(init.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
    print(init.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
    print(init.ladderLength("hot", "dog", ["hot", "dog"]))  # 0
