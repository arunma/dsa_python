def pair_sum_sorted_array(numbers, target):
    if not numbers:
        return None

    low = 0
    high = len(numbers) - 1
    result = []

    while low < high:
        val = numbers[low] + numbers[high]

        if val < target:
            low += 1
        elif val > target:
            high -= 1
        else:
            result.append([low, high])
            low += 1
            high -= 1

            while low < high and numbers[low] == numbers[low - 1]:
                low += 1
    return result


if __name__ == '__main__':
    # print(pair_sum_sorted_array([1, 2, 3, 4, 6], 6))  # [[2,4]]
    print(pair_sum_sorted_array([1, 2, 3, 5, 10], 7))  # [[1,3]]
