def equal_subset_sum_partition(nums):
    summ = sum(nums)
    if summ & 1:
        return []
    target = summ // 2
    # if target == 0 and len(nums) > 0:
    #     ret = [False] * len(nums)
    #     ret[0] = True
    #     return ret
    ret = equal_subset_sum_partition_inner(nums, target, 0, {}, [])
    if not ret:
        return []
    N = len(nums)
    result = [False] * N
    for i in ret:
        result[i] = True
    return result


def equal_subset_sum_partition_inner(nums, target, i, memo, curr):
    if (target, i) in memo:
        return memo[(target, i)]

    if i >= len(nums):
        return None

    if target == 0:
        return curr.copy()
    if target < 0:
        return None

    # pick or skip
    choose = equal_subset_sum_partition_inner(nums, target - nums[i], i + 1, memo, curr + [i])
    skip = equal_subset_sum_partition_inner(nums, target, i + 1, memo, curr)
    memo[(target, i)] = choose or skip
    return memo[(target, i)]


if __name__ == '__main__':
    # print(equal_subset_sum_partition(nums=[1, 5, 11, 5]))
    print(equal_subset_sum_partition(nums=[0, 0]))
    # print(equal_subset_sum_partition(nums=[100, 99, 3, 98, 1]))
    # print(canPartition(nums=[1, 2, 3, 5]))
    # print(canPartition(nums=[1, 2, 5]))
    # print(canPartition(nums=[1, 2, 3, 4, 5, 6, 7]))
    # print(canPartition(nums=[14, 9, 8, 4, 3, 2]))
