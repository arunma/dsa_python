import sys
from collections import defaultdict


class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ws = 0
        counts = defaultdict(int)
        max_len = -sys.maxsize
        for we in range(len(s)):
            counts[s[we]] += 1
            while (we - ws + 1) > len(counts):
                counts[s[ws]] -= 1
                if counts[s[ws]] == 0:
                    del counts[s[ws]]
                ws += 1
            max_len = max(max_len, we - ws + 1)
        return max_len


if __name__ == '__main__':
    init = LongestSubstringWithoutRepeatingCharacters()
    print(init.lengthOfLongestSubstring(s="abcabcbb"))  # 3
    print(init.lengthOfLongestSubstring(s="bbbbb"))  # 1
    print(init.lengthOfLongestSubstring(s="pwwkew"))  # 3
