import sys
from collections import defaultdict


class MinimumWindowSubstring:
    def minWindow(self, s: str, t: str) -> str:
        if not s or len(s) < len(t):
            return ''
        ws = 0
        cmap = defaultdict(int)
        for c in t:
            cmap[c] += 1

        matches = 0
        min_length = sys.maxsize
        min_str = ''

        for we, cwe in enumerate(s):
            if cwe in cmap:
                cmap[cwe] -= 1
                if cmap[cwe] == 0:
                    matches += 1
            while matches == len(cmap):
                cws = s[ws]
                if we - ws + 1 < min_length:
                    min_length = we - ws + 1
                    min_str = s[ws:we + 1]

                if cws in cmap:
                    cmap[cws] += 1
                    if cmap[cws] == 1:
                        matches -= 1
                ws += 1
        return min_str


if __name__ == '__main__':
    init = MinimumWindowSubstring()
    print(init.minWindow(s="BDABEBCODEBANCB", t="ABBC"))  # BANCB
    print(init.minWindow(s="ab", t="a"))  # a
    print(init.minWindow(s="a", t="b"))  # ''
    print(init.minWindow(s="ADOBECODEBANC", t="ABC"))  # BANC
    print(init.minWindow(s="a", t="a"))  # a
    print(init.minWindow(s="a", t="aa"))  # ''
    print(init.minWindow(s="aa", t="aa"))  # aa
    print(init.minWindow(s="cabwefgewcwaefgcf", t="cae"))  # cwae
