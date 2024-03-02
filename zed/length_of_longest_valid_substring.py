from typing import *


class LengthOfLongestValidSubstring:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        ws = 0
        forbidden = set(forbidden)
        max_length = float('-inf')
        for we in range(len(word)):
            for i in range(max(we - 10, ws), we + 1):
                if word[i:we + 1] in forbidden:
                    ws = i + 1
                    break
                max_length = max(max_length, i - ws + 1)
        return max_length

    # def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
    #     setF = set(forbidden)
    #     res = ws = 0
    #     for we in range(len(word)):
    #         for j in range(max(ws, we - 10), we + 1):
    #             if word[j:we + 1] in setF:
    #                 ws = j + 1
    #         res = max(res, we - ws + 1)
    #     return res


if __name__ == "__main__":
    init = LengthOfLongestValidSubstring()
    # print(init.longestValidSubstring("abc", ["ab", "bc"]))  # 1
    # print(init.longestValidSubstring(word="cbaaaabc", forbidden=["aaa", "cb"]))  # 4
    print(init.longestValidSubstring(word="leetcode", forbidden=["de", "le", "e"]))  # 4
