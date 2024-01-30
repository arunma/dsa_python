from typing import *


class SumOfSubarrayMinimums:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        stack = []  # (index, num)
        left = [0] * n
        right = [n] * n
        result = 0
        for i, num in enumerate(arr):
            while stack and num < stack[-1][1]:
                j, top = stack.pop()
                right[j] = i
            left[i] = stack[-1][0] if stack else -1
            stack.append((i, num))

        for i in range(n):
            result = (result + arr[i] * (i - left[i]) * (right[i] - i)) % MOD

        # for i in range(n):
        #     while stack and arr[i] < arr[stack[-1]]:
        #         right[stack.pop()] = i
        #     left[i] = stack[-1] if stack else -1
        #     stack.append(i)

        return result


if __name__ == '__main__':
    init = SumOfSubarrayMinimums()
    print(init.sumSubarrayMins([3, 1, 2, 4]))  # 17
