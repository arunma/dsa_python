def find_all_arrangements(n):
    result = []
    solve_n_queens(n, [], [], [], result)
    ret = []
    for board in result:
        board_ret = []
        for col in board:
            st = "-" * col + 'q' + "-" * (n - col - 1)
            board_ret.append(st)
        ret.append(board_ret)
    return ret


def solve_n_queens(n, placements, diag, anti_diag, result):
    if len(placements) == n:
        result.append(placements.copy())
        return

    row = len(placements)
    for col in range(n):
        if col not in placements and row + col not in diag and row - col not in anti_diag:
            solve_n_queens(n, placements + [col], diag + [row + col], anti_diag + [row - col], result)


if __name__ == '__main__':
    print(find_all_arrangements(4))
