def check_if_sum_possible(arr, k):
    return check_if_sum_possible_inner(arr, k, 0, 0)


def check_if_sum_possible_inner(arr, k, summ, index):
    # if k > 0 and (summ < 0 or summ > k):
    #     return False
    # if k < 0 and (summ > 0 or summ < k):
    #     return False
    if k == summ and index > 0:
        return True

    for i in range(index, len(arr)):
        if check_if_sum_possible_inner(arr, k, summ + arr[i], i + 1):
            return True
    return False


if __name__ == '__main__':
    print(check_if_sum_possible([2, 4, 8], 6))  # True
    print(check_if_sum_possible([2, 4, 6], 5))  # False
    print(check_if_sum_possible([2, 4, 6], 0))  # False
    print(check_if_sum_possible([-3, -3, -3, -3], -12))  # True
    print(check_if_sum_possible([10, 20], 0))  # False
    print(check_if_sum_possible([-2, -3, 1], -4))  # True
