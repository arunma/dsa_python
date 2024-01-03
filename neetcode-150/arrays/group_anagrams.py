from collections import defaultdict
from typing import *


class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for each in strs:
            sor = sorted(each)
            result[tuple(sor)].append(each)

        return list(result.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for each in strs:
            counts = [0] * 26
            for c in each:
                counts[ord(c) - ord('a')] += 1
            result[tuple(counts)].append(each)

        return list(result.values())


if __name__ == '__main__':
    init = GroupAnagrams()
    print(init.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(init.groupAnagrams(strs=[""]))  # [[""]]
    print(init.groupAnagrams(strs=["a"]))  # [["a"]]
