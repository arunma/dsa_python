from typing import *


class LengthOfLongestValidSubstring:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        return self.longest_valid_substring(word, forbidden, 0, "")

    def longest_valid_substring(self, word, forbidden):
        if not word:
            return 0
        if word in forbidden:
            return 0
        max_count = float('-inf')
        for ii in range(len(word)):
            with_count = self.longest_valid_substring(word[], forbidden)
            without_count = self.longest_valid_substring(word, forbidden, i + 1, curr)
            max_count = max(max_count, with_count, without_count)
        return max_count


if __name__ == '__main__':
    init = LengthOfLongestValidSubstring()
    # print(init.longestValidSubstring("abc", ["ab", "bc"]))  # 1
    print(init.longestValidSubstring(word="cbaaaabc", forbidden=["aaa", "cb"]))  # 4
    # print(init.longestValidSubstring(word="leetcode", forbidden=["de", "le", "e"]))  # 4
