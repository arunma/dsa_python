from typing import *


class MakeArrayZeroBySubtractingEqualAmounts:
    def minimumOperations(self, nums: List[int]) -> int:

        count = 0
        zeros = [0] * len(nums)
        while nums != zeros:
            mini = min([n for n in nums if n != 0])
            count += 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= mini
        return count


if __name__ == '__main__':
    init = MakeArrayZeroBySubtractingEqualAmounts()
    print(init.minimumOperations([1, 5, 0, 3, 5]))  # 3
