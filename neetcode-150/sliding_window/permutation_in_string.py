from collections import Counter
from typing import *


class PermutationInString:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = Counter(s1)
        N = len(s1)
        for we, swe in enumerate(s2):
            if swe in freq_map:
                freq_map[swe] -= 1
            if we > N - 1 and s2[we - N] in freq_map:
                freq_map[s2[we - N]] += 1
            if all(value <= 0 for value in freq_map.values()):
                return True
        return False


if __name__ == '__main__':
    init = PermutationInString()
    # print(init.checkInclusion(s1="ab", s2="eidbaooo"))  # True
    # print(init.checkInclusion(s1="ab", s2="eidboaoo"))  # False
    print(init.checkInclusion(s1="adc", s2="dcda"))  # True
