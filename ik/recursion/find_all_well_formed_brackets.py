def find_all_well_formed_brackets(n):
    if n == 0:
        return []
    result = []
    find_all_well_formed_brackets_inner(n, 0, 0, "", result)
    return result


def find_all_well_formed_brackets_inner(n, left, right, curr, result):
    if len(curr) == 2 * n:
        result.append(curr)
        return

    if left < n:
        find_all_well_formed_brackets_inner(n, left + 1, right, curr + '(', result)
    if right < left:
        find_all_well_formed_brackets_inner(n, left, right + 1, curr + ')', result)


def find_all_well_formed_brackets(n):
    stack = [("(", 1, 0)]
    result = []
    while stack:
        curr, left, right = stack.pop()
        if left == right == n:
            result.append(curr)
            continue
        if left < n:
            stack.append((curr + "(", left + 1, right))
        if right < left:
            stack.append((curr + ")", left, right + 1))
    return result


if __name__ == '__main__':
    print(find_all_well_formed_brackets(3))
