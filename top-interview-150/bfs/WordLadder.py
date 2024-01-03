from collections import deque
from typing import *


class WordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        queue = deque([(beginWord, 0)])
        seen = set()
        while queue:
            curr, dist = queue.popleft()
            if curr == endWord:
                return dist + 1

            for dict_word in wordList:
                if dict_word not in seen and self.is_one_step_apart(curr, dict_word):
                    queue.append((dict_word, dist + 1))
                    seen.add(dict_word)

        return 0

    def is_one_step_apart(self, start, end):
        dist = 0
        for s, e in zip(start, end):
            if s != e:
                dist += 1
        return dist == 1


if __name__ == '__main__':
    init = WordLadder()
    print(init.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
    print(init.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))  # 0
