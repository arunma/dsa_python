from collections import defaultdict
from typing import *


class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for st in strs:
            map[str(sorted(st))].append(st)

        return [v for k, v in map.items()]


if __name__ == '__main__':
    init = GroupAnagrams()
    print(init.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(init.groupAnagrams(strs=[""]))  # [[""]]
    print(init.groupAnagrams(strs=["a"]))  # [["a"]]
