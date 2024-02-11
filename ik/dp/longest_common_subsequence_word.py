# def longestCommonSubsequence(self, word1: str, word2: str) -> int:
#     return self.longest_common_subsequence(word1, word2, 0, 0, [])
#
# def longest_common_subsequence(self, word1, word2, i, j, curr):
#     if i == len(word1) or j == len(word2):
#         return ''.join(curr)
#
#     if word1[i] == word2[j]:
#         return self.longest_common_subsequence(word1, word2, i + 1, j + 1, curr + [word1[i]])
#     else:
#         choose_left = self.longest_common_subsequence(word1, word2, i + 1, j, curr)
#         choose_right = self.longest_common_subsequence(word1, word2, i, j + 1, curr)
#         return max(choose_left, choose_right, key=len)

def lcs(word1, word2):
    ret = lcs_inner(word1, word2, 0, 0, [], {})
    if not ret:
        return "-1"
    return ret


def lcs_inner(word1, word2, i, j, curr, memo):
    if i == len(word1) or j == len(word2):
        return ''.join(curr)

    if (i, j, tuple(curr)) in memo:
        return memo[(i, j, tuple(curr))]

    if word1[i] == word2[j]:
        ret = lcs_inner(word1, word2, i + 1, j + 1, curr + [word1[i]], memo)
        memo[(i, j, tuple(curr))] = ret
        return ret
    else:
        choose_left = lcs_inner(word1, word2, i + 1, j, curr, memo)
        choose_right = lcs_inner(word1, word2, i, j + 1, curr, memo)
        ret = max(choose_left, choose_right, key=len)
        memo[(i, j, tuple(curr))] = ret
        return ret


if __name__ == '__main__':
    print(lcs(word1="abcde", word2="ace"))  # ace
    print(lcs(word1="abc", word2="abc"))  # abc
    print(lcs(word1="ABCDE", word2="AECBD"))  # ABD
