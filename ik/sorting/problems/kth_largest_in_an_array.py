def kth_largest_in_an_array(numbers, k):
    N = len(numbers)
    low = 0
    high = N - 1
    return quick_select(numbers, N - k, low, high)


def quick_select(numbers, k, low, high):
    # if low == high:
    #     return numbers[low]

    if low <= high:
        part = partition(numbers, low, high)
        if part == k:
            return numbers[part]
        elif part < k:
            while part < k and numbers[part] == numbers[part - 1]:
                part += 1
            return quick_select(numbers, k, part + 1, high)
        else:
            while part > low and numbers[part] == numbers[part + 1]:
                part -= 1
            return quick_select(numbers, k, low, part - 1)


def partition(numbers, low, high):
    pivot = high
    low_pos = low
    for i in range(low, high):
        if numbers[i] < numbers[pivot]:
            numbers[low_pos], numbers[i] = numbers[i], numbers[low_pos]
            low_pos += 1
    numbers[low_pos], numbers[pivot] = numbers[pivot], numbers[low_pos]
    return low_pos


if __name__ == '__main__':
    print(kth_largest_in_an_array([5, 1, 10, 3, 2], 2))  # 5
    print(kth_largest_in_an_array([2, 1], 1))  # 2
