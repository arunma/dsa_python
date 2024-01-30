def generate_all_combinations(arr, target):
    result = []
    arr.sort()
    generate_all_combinations_inner(arr, target, 0, [], 0, result)
    return result


def generate_all_combinations_inner(arr, target, index, curr, summ, result):
    if summ > target or summ < 0:
        return
    if summ == target:
        result.append(curr.copy())
        return

    for i in range(index, len(arr)):
        if i != index and arr[i] == arr[i - 1]:
            continue
        generate_all_combinations_inner(arr, target, i + 1, curr + [arr[i]], summ + arr[i], result)


if __name__ == '__main__':
    print(generate_all_combinations([1, 2, 3], 3))  # [[1, 2], [3]]
    print(generate_all_combinations([1, 1, 1, 1], 2))  # [[1, 1]]
