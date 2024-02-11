class LongestCommonSubsequence:
    def longestCommonSubsequence(self, word1: str, word2: str) -> int:
        return self.longest_common_subsequence(word1, word2, 0, 0)

    def longest_common_subsequence(self, word1, word2, i, j):
        if i == len(word1) or j == len(word2):
            return 0

        if word1[i] == word2[j]:
            return 1 + self.longest_common_subsequence(word1, word2, i + 1, j + 1)
        else:
            choose_left = self.longest_common_subsequence(word1, word2, i + 1, j)
            choose_right = self.longest_common_subsequence(word1, word2, i, j + 1)
            return max(choose_left, choose_right)

    # Memo
    def longestCommonSubsequence(self, word1: str, word2: str) -> int:
        return self.longest_common_subsequence(word1, word2, 0, 0, {})

    def longest_common_subsequence(self, word1, word2, i, j, memo):
        if i == len(word1) or j == len(word2):
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        if word1[i] == word2[j]:
            ret = 1 + self.longest_common_subsequence(word1, word2, i + 1, j + 1, memo)
            memo[(i, j)] = ret
            return ret
        else:
            choose_left = self.longest_common_subsequence(word1, word2, i + 1, j, memo)
            choose_right = self.longest_common_subsequence(word1, word2, i, j + 1, memo)
            ret = max(choose_left, choose_right)
            memo[(i, j)] = ret
            return ret


if __name__ == '__main__':
    init = LongestCommonSubsequence()
    print(init.longestCommonSubsequence(word1="abcde", word2="ace"))  # 3
    print(init.longestCommonSubsequence(word1="abc", word2="abc"))  # 3
# {
# "a": "ABCDE",
# "b": "AECBD"
# }
