from typing import *


class LengthOfLongestValidSubstring:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        ws = 0
        max_len = float('-inf')
        max_word = ""
        for we in range(len(word)):
            for i in range(max(ws, we - 10), we + 1):
                print(f"i: {i}, we: {we}")
                if word[i:we + 1] in forbidden:
                    ws = i + 1
                    break
                max_word = max(max_word, word[ws:i + 1], key=len)
                max_len = max(max_len, i - ws + 1)
            print("----")
        print(f"maxword: {max_word}")
        return max_len


if __name__ == '__main__':
    init = LengthOfLongestValidSubstring()
    # print(init.longestValidSubstring("abc", ["ab", "bc"]))  # 1
    print(init.longestValidSubstring(word="cbaaaabc", forbidden=["aaa", "cb"]))  # 4
    # print(init.longestValidSubstring(word="leetcode", forbidden=["de", "le", "e"]))  # 4
