def generate_all_subsets(s):
    if not s:
        return [""]
    result = []
    generate_subsets_inner(s, 0, "", result)
    return result


def generate_subsets_inner(s, index, curr, result):
    if index == len(s):
        result.append(curr)
        return
    generate_subsets_inner(s, index + 1, curr, result)
    generate_subsets_inner(s, index + 1, curr + s[index], result)


if __name__ == '__main__':
    print(generate_all_subsets("xy"))
