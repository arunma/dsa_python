MOD = (10 ** 9 + 7)


def count_phone_numbers_of_given_length(s, n):
    R = 4
    C = 3
    ret_count = 0

    map = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}
    (r, c) = map[s]
    ret_count = (ret_count + knight_dialer(n, r, c, {})) % MOD
    return ret_count


def knight_dialer(n, r, c, memo):
    if r < 0 or c < 0 or r > 3 or c > 2 or (r == 3 and c != 1):
        return 0

    if n == 1:
        return 1

    if (n, r, c) in memo:
        return memo[(n, r, c)]

    total_counts = 0
    total_counts += (
            knight_dialer(n - 1, r + 1, c + 2, memo) % MOD +
            knight_dialer(n - 1, r - 1, c + 2, memo) % MOD +
            knight_dialer(n - 1, r + 1, c - 2, memo) % MOD +
            knight_dialer(n - 1, r - 1, c - 2, memo) % MOD +
            knight_dialer(n - 1, r + 2, c + 1, memo) % MOD +
            knight_dialer(n - 1, r - 2, c + 1, memo) % MOD +
            knight_dialer(n - 1, r + 2, c - 1, memo) % MOD +
            knight_dialer(n - 1, r - 2, c - 1, memo) % MOD
    )

    memo[(n, r, c)] = total_counts % MOD
    return memo[(n, r, c)]


if __name__ == '__main__':
    print(count_phone_numbers_of_given_length(1, 2))
    print(count_phone_numbers_of_given_length(1, 3))
