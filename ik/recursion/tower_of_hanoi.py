def tower_of_hanoi(n):
    start = list(range(1, n + 1))
    result = []
    solve(start, [], [], n, result)
    return result


def move_one_disk(start, end, result):
    disk = start.pop()
    end.append(disk)
    result.append([start, end].copy())


def solve(start, end, temp, n, result):
    if n == 1:
        move_one_disk(start, end, result)
        return
    else:
        solve(start, temp, end, n - 1, result)
        move_one_disk(start, end, result)
        solve(temp, end, start, n - 1, result)
        return


if __name__ == '__main__':
    print(tower_of_hanoi(4))
