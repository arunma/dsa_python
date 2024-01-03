# count triplets less than target
def count_triplets(target, numbers):
    if not numbers:
        return None

    count = 0
    numbers.sort()
    for i, third in enumerate(numbers):
        if third > target:
            break
        count += two_sum(numbers, target, third, i + 1)
    return count


def two_sum(numbers, target, third, i):
    low = i
    high = len(numbers) - 1
    count = 0

    while low < high:
        val = third + numbers[low] + numbers[high]
        if val < target:
            # result.add(tuple(sorted([third, numbers[low], numbers[high]])))
            count += (high - low)
            low += 1
        else:
            high -= 1
    return count


if __name__ == '__main__':
    print(count_triplets(4, [5, 0, -1, 3, 2]))
