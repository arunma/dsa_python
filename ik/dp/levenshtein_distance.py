import sys


def levenshtein_distance(word1, word2):
    R = len(word1)
    C = len(word2)
    dp = [[sys.maxsize] * (C + 1) for _ in range(R + 1)]
    for r in range(R + 1):
        dp[r][0] = r
    for c in range(C + 1):
        dp[0][c] = c

    dp[0][0] = 0

    for i in range(1, R + 1):
        for j in range(1, C + 1):
            c1, c2 = word1[i - 1], word2[j - 1]
            if c1 != c2:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            else:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[-1][-1]


def levenshtein_distance(word1, word2):
    return levenshtein_distance_inner(word1, word2, 0, 0, {})


def levenshtein_distance_inner(word1, word2, i, j, memo):
    if i == len(word1) and j == len(word2):
        return 0
    if i == len(word1):
        return len(word2) - j
    if j == len(word2):
        return len(word1) - i
    if (i, j) in memo:
        return memo[(i, j)]

    count = 0
    if word1[i] == word2[j]:
        count += levenshtein_distance_inner(word1, word2, i + 1, j + 1, memo)
    else:
        insert = 1 + levenshtein_distance_inner(word1, word2, i, j + 1, memo)
        delete = 1 + levenshtein_distance_inner(word1, word2, i + 1, j, memo)
        replace = 1 + levenshtein_distance_inner(word1, word2, i + 1, j + 1, memo)
        count += min(insert, delete, replace)

    memo[(i, j)] = count
    return count


if __name__ == '__main__':
    print(levenshtein_distance("cat", "bat"))  # 1
    print(levenshtein_distance("qwe", "q"))  # 2
    print(levenshtein_distance('horse', 'ros'))  # 3
    print(levenshtein_distance('intention', 'execution'))  # 5
    print(levenshtein_distance('intention', 'intention'))  # 0
