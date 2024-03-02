from typing import *


class WordBreak:
    # def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    #     result = []
    #     wordDict = set(wordDict)
    #     self.word_break(s, wordDict, [], 0, result)
    #     return result
    #
    # def word_break(self, s, word_dict, curr, index, result):
    #     if index == len(s):
    #         result.append(curr.copy())
    #         return
    #
    #     for i in range(index, len(s)):
    #         for j in range(i + 1, len(s)):
    #             print(s[j:i])
    #             if s[j:i] in word_dict:
    #                 self.word_break(s, word_dict, curr + [s[j:i]], i, result)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        wordDict = set(wordDict)
        self.word_break(s, wordDict, [], result)
        return result

    def word_break(self, s, word_dict, curr, result):
        if not s:
            result.append(' '.join(curr.copy()))
            return

        for word in word_dict:
            if s.startswith(word):
                self.word_break(s[len(word):], word_dict, curr + [word], result)


if __name__ == "__main__":
    init = WordBreak()
    print(init.wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))  # ["cats and dog", "cat sand dog"]
    print(init.wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine",
                                                          "pineapple"]))  # ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    print(init.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))  # []
