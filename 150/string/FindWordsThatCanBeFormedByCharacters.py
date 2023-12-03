from collections import Counter
from typing import *


class FindWordsThatCanBeFormedByCharacters:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cfreq = Counter(chars)
        result = 0

        for word in words:
            wfreq = Counter(word)

            match = True
            for key, freq in wfreq.items():
                if cfreq[key] < freq:
                    match = False
                    break
            if match:
                result += len(word)

        return result


if __name__ == '__main__':
    init = FindWordsThatCanBeFormedByCharacters()
    print(init.countCharacters(["cat", "bt", "hat", "tree"], "atach"))  # 6
    print(init.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))  # 10
