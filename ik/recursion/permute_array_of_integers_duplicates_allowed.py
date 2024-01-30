def get_permutations(arr):
    result = []
    # arr.sort()
    visited = set()
    get_permutations_inner(arr, visited, [], result)
    return result


# def get_permutations_inner(arr, visited, curr, result):
#     if len(curr) == len(arr):
#         result.append(curr.copy())
#         return
#
#     for i in range(len(arr)):
#         if i in visited or (i > 0 and arr[i] == arr[i - 1] and i - 1 in visited):
#             continue
#         visited.add(i)
#         get_permutations_inner(arr, visited, curr + [arr[i]], result)
#         visited.remove(i)


def get_permutations(nums):
    result = []
    nums.sort()
    get_permutations_inner(nums, [], result)
    return result


def get_permutations_inner(nums, curr, result):
    if not nums:
        result.append(curr.copy())
        return

    for i in range(len(nums)):
        get_permutations_inner(nums[:i] + nums[i + 1:], curr + [nums[i]], result)


# def get_permutations(nums):
#     result = []
#     get_permutations_inner(nums, 0, result)
#     return result


# def get_permutations_inner(nums, index, result):
#     if index == len(nums):
#         result.append(nums.copy())
#         return
#
#     visited = set()
#     for i in range(index, len(nums)):
#         if nums[i] in visited:
#             continue
#         visited.add(nums[i])
#         # if i in visited:
#         #     continue
#         # visited.add(i)
#         nums[i], nums[index] = nums[index], nums[i]
#         get_permutations_inner(nums, index + 1, result)
#         nums[index], nums[i] = nums[i], nums[index]
#         # visited.remove(nums[i])

def get_permutations(nums):
    result = []
    nums.sort()
    visited = set()
    get_permutations_inner(nums, [], visited, result)
    return result


def get_permutations_inner(nums, curr, visited, result):
    if len(curr) == len(nums):
        result.append(curr.copy())
        return

    for i in range(len(nums)):
        if i in visited or (i > 0 and nums[i] == nums[i - 1] and i - 1 in visited):
            continue
        visited.add(i)
        get_permutations_inner(nums, curr + [nums[i]], visited, result)
        visited.remove(i)


if __name__ == '__main__':
    # print(get_permutations([1, 2, 2]))
    print(get_permutations([1, 2, 1]))
    # print(get_permutations([1, 7]))
    # print(get_permutations([4, 7, 4, 4]))
