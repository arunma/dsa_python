def generate_palindromic_decompositions(s):
    result = []
    generate_palindrome_inner(s, [], result)
    return result


def generate_palindrome_inner(s, curr, result):
    if not s:
        result.append("|".join(curr))
        return

    for i in range(1, len(s) + 1):
        if is_palin(s[:i]):
            generate_palindrome_inner(s[i:], curr + [s[:i]], result)


def is_palin(s):
    return s[::] == s[::-1]


if __name__ == '__main__':
    print(generate_palindromic_decompositions("aab"))
    print(generate_palindromic_decompositions("abracadabra"))
