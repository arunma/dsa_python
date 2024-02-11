from typing import List


class WordBreakII:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        self.word_break_inner(s, wordDict, [], result)
        return result

    def word_break_inner(self, s, wordDict, curr, result):
        if not s:
            result.append(' '.join(curr))
            return
        for word in wordDict:
            if s.startswith(word):
                self.word_break_inner(s[len(word):], wordDict, curr + [word], result)
        return


if __name__ == '__main__':
    init = WordBreakII()
    print(init.wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))  # ["cats and dog","cat sand dog"]
    print(init.wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine",
                                                          "pineapple"]))  # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
    print(init.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))  # []
