from typing import *


class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        N = len(s)
        max_str = ""
        for i in range(1, N):
            str1 = self.expand_from_center(s, i, i)
            str2 = self.expand_from_center(s, i, i - 1)
            max_str = max(max_str, str1, str2, key=len)
        return max_str

    def expand_from_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        N = len(s)
        max_str = s[0]
        for i in range(1, N):
            l1, r1 = self.expand_from_center(s, i, i)
            l2, r2 = self.expand_from_center(s, i, i - 1)
            if r1 - l1 > r2 - l2:
                max_str = max(max_str, s[l1:r1], key=len)
            elif r2 - l2 > len(max_str):
                max_str = max(max_str, s[l2:r2], key=len)
        return max_str

    def expand_from_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right


if __name__ == "__main__":
    init = LongestPalindromicSubstring()
    print(init.longestPalindrome("babad"))  # "bab" or "aba"
    print(init.longestPalindrome("cbbd"))  # "bb"
    print(init.longestPalindrome("ac"))  # "a"
