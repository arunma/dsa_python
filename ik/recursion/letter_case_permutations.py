def letter_case_permutations(s):
    result = []
    letter_case_permutations_inner(s, "", 0, result)
    return result


def letter_case_permutations_inner(s, curr, i, result):
    if len(curr) == len(s):
        result.append(curr)
        return

    if s[i].isalpha():
        letter_case_permutations_inner(s, curr + s[i].upper(), i + 1, result)
        letter_case_permutations_inner(s, curr + s[i].lower(), i + 1, result)
    else:
        letter_case_permutations_inner(s, curr + s[i], i + 1, result)

    # if i < len(s) and s[i].isalpha():
    #    letter_case_permutations_inner(s[:i] + s[i + 1:], curr + s[i].upper(), i + 1, result)
    #    letter_case_permutations_inner(s[:i] + s[i + 1:], curr + s[i].lower(), i + 1, result)


if __name__ == '__main__':
    print(letter_case_permutations("a1z"))
