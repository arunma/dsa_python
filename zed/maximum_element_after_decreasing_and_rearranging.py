from typing import *


class MaximumElementAfterDecreasingAndRearranging:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maxi = 1
        for i in range(1, len(arr)):
            # print(arr[i], maxi)
            if arr[i] > maxi:
                maxi += 1
        return maxi

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        N = len(arr)
        count = [0] * (N + 1)
        for num in arr:
            count[min(num, N)] += 1

        maxi = 1
        for num in range(2, len(count)):
            if num < count[num]:
                maxi = num
            else:
                maxi += count[num]
        return maxi

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        N = len(arr)
        count = [0] * (N + 1)
        for num in arr:
            count[min(num, N)] += 1

        maxi = 1
        for num in range(2, len(count)):
            maxi = min(num, maxi + count[num])
        return maxi


if __name__ == "__main__":
    init = MaximumElementAfterDecreasingAndRearranging()
    # print(init.maximumElementAfterDecrementingAndRearranging(arr=[1, 3, 4, 5]))  # 4
    # print(init.maximumElementAfterDecrementingAndRearranging(arr=[1, 1, 2, 4, 1]))  # 3
    # print(init.maximumElementAfterDecrementingAndRearranging(arr=[2, 2, 1, 2, 1]))  # 2
    # print(init.maximumElementAfterDecrementingAndRearranging(arr=[100, 1, 1000]))  # 3
    # print(init.maximumElementAfterDecrementingAndRearranging(arr=[1, 2, 3, 4, 5]))  # 5
    # print(init.maximumElementAfterDecrementingAndRearranging(arr=[1, 1, 1, 1, 1]))  # 1
    print(init.maximumElementAfterDecrementingAndRearranging(arr=[73, 98, 9]))  # 3
