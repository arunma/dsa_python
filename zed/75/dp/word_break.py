from typing import *


class WordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
        wordDict = set(wordDict)

        for i in range(N + 1):
            for j in range(i + 1):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
        return dp[-1]


if __name__ == "__main__":
    init = WordBreak()
    print(init.wordBreak(s="leetcode", wordDict=["leet", "code"]))  # True
    # print(init.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))  # True
    # print(init.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))  # False
