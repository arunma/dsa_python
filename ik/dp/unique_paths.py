def unique_paths(n, m):
    return unique_paths_inner(n, m, 0, 0)


def unique_paths_inner(n, m, i, j):
    if i == n - 1 and j == m - 1:
        return 1

    if i == n or j == m:
        return 0

    counts = unique_paths_inner(n, m, i + 1, j) + unique_paths_inner(n, m, i, j + 1)
    return counts


def unique_paths(n, m):
    return unique_paths_inner(n, m, 0, 0, {})


def unique_paths_inner(n, m, i, j, memo):
    if (i, j) in memo:
        return memo[(i, j)]

    if i == n - 1 and j == m - 1:
        return 1
    if i == n or j == m:
        return 0

    counts = (unique_paths_inner(n, m, i + 1, j, memo) + unique_paths_inner(n, m, i, j + 1, memo)) % (10 ** 9 + 7)
    memo[(i, j)] = counts
    return counts


if __name__ == '__main__':
    print(unique_paths(3, 2))
