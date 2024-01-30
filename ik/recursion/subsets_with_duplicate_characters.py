# def get_distinct_subsets(s):
#     result = []
#     get_distinct_subsets_inner(s, 0, [], result)
#     return result
#
#
# def get_distinct_subsets_inner(s, index, curr, result):
#     if index == len(s):
#         result.append(''.join(curr))
#         return
#
#     get_distinct_subsets_inner(s, index + 1, curr, result)
#     get_distinct_subsets_inner(s, index + 1, curr + [s[index]], result)


def get_distinct_subsets(s):
    result = []
    s = list(s)
    s.sort()
    get_distinct_subsets_inner(s, 0, "", result)
    return result


def get_distinct_subsets_inner(s, index, curr, result):
    result.append(curr)
    for i in range(index, len(s)):
        if i != index and s[i] == s[i - 1]:
            continue
        get_distinct_subsets_inner(s, i + 1, curr + s[i], result)


if __name__ == '__main__':
    print(get_distinct_subsets("aab"))
