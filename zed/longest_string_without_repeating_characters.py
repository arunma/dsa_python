from collections import defaultdict
from typing import *


class LongestStringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ws = 0
        mapp = defaultdict(int)
        max_length = float('-inf')
        max_word = ""
        for we in range(len(s)):
            mapp[s[we]] += 1
            while we - ws + 1 > len(mapp):
                mapp[s[ws]] -= 1
                if mapp[s[ws]] == 0:
                    del mapp[s[ws]]
                ws += 1
            max_word = max(max_word, s[ws:we + 1], key=len)
            max_length = max(max_length, we - ws + 1)

        return max_length if max_length > float('-inf') else 0

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ws = 0
        mapp = defaultdict(int)
        max_length = float('-inf')
        for we in range(len(s)):
            mapp[s[we]] += 1
            while we - ws + 1 > len(mapp):
                mapp[s[ws]] -= 1
                if mapp[s[ws]] == 0:
                    del mapp[s[ws]]
                ws += 1
            max_length = max(max_length, we - ws + 1)

        return max_length if max_length > float('-inf') else 0

    def sliding_window_problem(self, s: str) -> int:
        if not s:
            return 0
        # ws = window start, we=window end
        ws = 0
        freq_map = defaultdict(int)
        result = ...
        for we in range(len(s)):  # for loop with we (window end)
            freq_map[s[we]] += 1  # increment frequency map
            while we - ws + 1 > len(freq_map):  # while loop
                freq_map[s[ws]] -= 1  # decrement freq map
                # any other conditions and cleanup here
                ws += 1  # increment ws
            max_length = max(max_length, we - ws + 1)  # update result outside the while loop

        return max_length if max_length > float('-inf') else 0


if __name__ == "__main__":
    init = LongestStringWithoutRepeatingCharacters()
    print(init.lengthOfLongestSubstring(s="abcabcbb"))  # 3
    print(init.lengthOfLongestSubstring(s="bbbbb"))  # 1
    print(init.lengthOfLongestSubstring(s="pwwkew"))  # 3
    print(init.lengthOfLongestSubstring(s=""))  # 0
    print(init.lengthOfLongestSubstring(s=" "))  # 0
