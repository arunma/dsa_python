from collections import defaultdict


def four_sum(arr, target):
    sum_map = defaultdict(list)
    N = len(arr)
    for i in range(N):
        for j in range(i + 1, N):
            sum_map[arr[i] + arr[j]].append((i, j))

    result = set()
    for i in range(N):
        for j in range(i + 1, N):
            summ = arr[i] + arr[j]
            if target - summ in sum_map:
                for ii, jj in sum_map[target - summ]:
                    if (i != ii and j != jj) and (i != jj and j != ii):
                        result.add(tuple(sorted([arr[i], arr[j], arr[ii], arr[jj]])))
    return result


if __name__ == '__main__':
    # print(four_sum([1, 0, -1, 0, -2, 2], 0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    # print(four_sum([2, 2, 2, 2, 2], 8))  # [[2,2,2,2]]
    print(four_sum([0, 0, 1, 3, 2, -1], 3))  # [[-1,0,1,3], [0,0,1,2]]]
