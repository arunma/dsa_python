def word_break(s, dictionary):
    return word_break_inner(s, dictionary, {})


def word_break_inner(s, dictionary, memo):
    if s in memo:
        return memo[s]
    if not s:
        return True

    for word in dictionary:
        if s.startswith(word):
            if word_break_inner(s[len(word):], dictionary, memo):
                return True
    memo[s] = False
    return False


if __name__ == '__main__':
    print(word_break("leetcode", ["leet", "code"]))  # True
    print(word_break("applepenapple", ["apple", "pen"]))  # True
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
