from collections import defaultdict, deque
from typing import *


class WordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                word_dict[key].append(word)
        queue = deque([(beginWord, 1)])
        seen = set()
        while queue:
            word, dist = queue.popleft()
            seen.add(word)
            if word == endWord:
                return dist
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                for nei in word_dict[key]:
                    if nei not in seen:
                        queue.append((nei, dist + 1))
        return 0


if __name__ == '__main__':
    init = WordLadder()
    print(init.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
    print(init.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
