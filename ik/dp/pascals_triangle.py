def find_pascal_triangle(n):
    result = []
    for i in range(n):
        result.append([1] * (i + 1))

    R = n
    # C = 1
    for r in range(1, R):
        for c in range(1, r):
            pr, pc = r - 1, c - 1
            nr, nc = r - 1, c
            result[r][c] = result[pr][pc] + result[nr][nc]
            # if -1 < pr < R and -1 < pc < C:
            #     result[r][c] += result[pr][pc]
            # if -1 < nr < R and -1 < nc < C:
            #     result[r][c] += result[nr][nc]
        # C += 1

    return result


if __name__ == '__main__':
    init = find_pascal_triangle(4)
    print(init)  # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
