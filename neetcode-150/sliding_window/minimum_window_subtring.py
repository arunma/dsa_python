from collections import Counter
from typing import *


class MinimumWindowSubtring:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq_map = Counter(t)

        matches = 0
        ws = 0
        min_length = float('inf')
        min_string = ""
        for we, swe in enumerate(s):
            if swe in freq_map:
                freq_map[swe] -= 1
                if freq_map[swe] == 0:
                    matches += 1

                while matches == len(freq_map):
                    sws = s[ws]
                    if we - ws + 1 < min_length:
                        min_length = we - ws + 1
                        min_string = s[ws:we + 1]

                    if sws in freq_map:
                        freq_map[sws] += 1
                        if freq_map[sws] > 0:
                            matches -= 1
                    ws += 1

        return "" if min_length == float('inf') else min_string


if __name__ == '__main__':
    init = MinimumWindowSubtring()
    print(init.minWindow(s="ADOBECODEBANC", t="ABC"))  # "BANC"
    print(init.minWindow(s="a", t="a"))  # "a"
    print(init.minWindow(s="a", t="aa"))  # ""
