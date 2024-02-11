MOD = (10 ** 9 + 7)


def word_break_count(dictionary, txt):
    if not txt:
        return 1
    word_counts = 0
    for word in dictionary:
        if txt.startswith(word):
            remaining = txt[len(word):]
            word_counts = (word_counts + word_break_count(dictionary, remaining)) % MOD
    return word_counts


def word_break_count(dictionary, txt, memo={}):
    if not txt:
        return 1
    if txt in memo:
        return memo[txt]
    word_counts = 0
    for word in dictionary:
        if txt.startswith(word):
            remaining = txt[len(word):]
            word_counts = (word_counts + word_break_count(dictionary, remaining, memo)) % MOD
    memo[txt] = word_counts
    return word_counts


if __name__ == '__main__':
    print(word_break_count(["kick", "start", "kickstart", "is", "awe", "some", "awesome"], "kickstartisawesome"))  # 4
