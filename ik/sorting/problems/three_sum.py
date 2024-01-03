def find_zero_sum(arr):
    if not arr:
        return None

    result = set()
    arr.sort()

    for i, target in enumerate(arr):
        if target > 0:
            break
        two_sum(arr, -target, i + 1, result)

    return list(result)


def two_sum(arr, target, i, result):
    low = i
    high = len(arr) - 1

    while low < high:
        val = arr[low] + arr[high]
        if val < target:
            low += 1
        elif val > target:
            high -= 1
        else:
            result.add(f"{-target},{arr[low]},{arr[high]}")
            low += 1
            high -= 1


def find_zero_sum(arr):
    if not arr:
        return None

    result = []
    arr.sort()

    for i, target in enumerate(arr):
        if target > 0:
            break
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        two_sum(arr, -target, i + 1, result)

    return result


def two_sum(arr, target, i, result):
    low = i
    high = len(arr) - 1

    while low < high:
        val = arr[low] + arr[high]
        if val < target:
            low += 1
        elif val > target:
            high -= 1
        else:
            result.append(f"{-target},{arr[low]},{arr[high]}")
            low += 1
            high -= 1
            while low < high and arr[low] == arr[low - 1]:
                low += 1


if __name__ == '__main__':
    print(find_zero_sum([10, 3, -4, 1, -6, 9]))
