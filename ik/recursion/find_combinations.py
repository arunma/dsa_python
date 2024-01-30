def find_combinations(n, k):
    nums = list(range(1, n + 1))
    result = []
    find_combinations_inner(nums, k, [], 0, result)
    # find_combinations_inner(nums, k, [], result)
    return result


def find_combinations_inner(nums, k, curr, index, result):
    # print('curr', curr, 'index', index, 'result', result)
    if len(curr) == k:
        result.append(curr.copy())
        return
    for i in range(index, len(nums)):
        find_combinations_inner(nums, k, curr + [nums[i]], i + 1, result)


# def find_combinations_inner(nums, k, curr, result):
#     if len(curr) == k:
#         result.append(curr.copy())
#         return
#     for i in range(len(nums)):
#         find_combinations_inner(nums[i + 1:], k, curr + [nums[i]], result)


if __name__ == '__main__':
    # print(find_combinations(5, 2))  # [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
    # print(find_combinations(6, 6))  # [[1, 2, 3, 4, 5, 6]]
    print(find_combinations(6, 3))  # [[1, 2, 3, 4, 5, 6]]
