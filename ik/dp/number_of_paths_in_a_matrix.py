def number_of_paths(matrix):
    R = len(matrix) - 1
    C = len(matrix[0]) - 1
    if matrix[R][C] == 0:
        return 0
    return number_of_paths_inner(matrix, 0, 0, R, C)


def number_of_paths_inner(matrix, r, c, R, C):
    if r == R and c == C:
        return 1
    if r < 0 or r > R or c < 0 or c > C or matrix[r][c] == 0:
        return 0
    neis = [(r + 1, c), (r, c + 1)]
    count = 0
    for nr, nc in neis:
        count += number_of_paths_inner(matrix, nr, nc, R, C)
    return count


def number_of_paths(matrix):
    R = len(matrix) - 1
    C = len(matrix[0]) - 1
    if matrix[R][C] == 0:
        return 0
    return number_of_paths_inner(matrix, 0, 0, R, C, {})


def number_of_paths_inner(matrix, r, c, R, C, memo):
    if (r, c) in memo:
        return memo[(r, c)]
    if r == R and c == C:
        return 1
    if r < 0 or r > R or c < 0 or c > C or matrix[r][c] == 0:
        return 0
    neis = [(r + 1, c), (r, c + 1)]
    count = 0
    for nr, nc in neis:
        count = (count + number_of_paths_inner(matrix, nr, nc, R, C, memo)) % (10 ** 9 + 7)
    memo[(r, c)] = count

    return count


def number_of_paths(matrix):
    R = len(matrix)
    C = len(matrix[0])

    for r in range(R):
        for c in range(C):
            if r == 0:
                matrix[0][c] = 1
            elif c == 0:
                matrix[r][0] = 1
            elif r != 0 and c != 0:
                up = 0
                left = 0
                if r - 1 >= 0:
                    up = matrix[r - 1][c]
                if c - 1 >= 0:
                    left = matrix[r][c - 1]
                matrix[r][c] = up + left
    print(matrix)
    return matrix[-1][-1]


if __name__ == '__main__':
    print(number_of_paths([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))  # 10
    print(number_of_paths([[1, 1], [0, 1]]))  # 1
