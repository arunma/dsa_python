from typing import *


class CharacterReplacement:
    def characterReplacement(self, s: str, k: int) -> int:
        ws=0
        for we in range(len(s)):



if __name__ == '__main__':
    init = CharacterReplacement()
    print(init.characterReplacement(s="ABAB", k=2))  # 4
    print(init.characterReplacement(s="AABABBA", k=1))  # 4
    print(init.characterReplacement(s="AAAA", k=0))  # 4
    print(init.characterReplacement(s="ABAA", k=0))  # 2
