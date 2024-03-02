from typing import *


class MakeArrayZeroBySubtractingEqualAmounts:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)
        zeros = [0] * N
        count = 0
        while nums != zeros:
            mini = min([num for num in nums if num != 0])
            count += 1
            for i in range(N):
                if nums[i] != 0:
                    nums[i] -= mini
        return count


if __name__ == "__main__":
    init = MakeArrayZeroBySubtractingEqualAmounts()
    print(init.minimumOperations([1, 5, 0, 3, 5]))  # 3
    print(init.minimumOperations([1, 1, 1, 1]))  # 1
