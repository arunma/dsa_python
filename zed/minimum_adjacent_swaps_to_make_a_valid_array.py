from typing import *


class MinimumAdjacentSwapsToMakeAValidArray:
    def minimumSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        mini = min(nums)
        lpos = nums.index(mini)
        nums = [nums[lpos]] + nums[:lpos] + nums[lpos + 1:]

        maxi = max(nums)
        rpos = nums[::-1].index(maxi)

        return rpos + lpos


if __name__ == "__main__":
    init = MinimumAdjacentSwapsToMakeAValidArray()
    print(init.minimumSwaps([3, 4, 5, 5, 3, 1]))  # 6
    print(init.minimumSwaps([1, 3, 5, 4, 2]))  # 2
    print(init.minimumSwaps([1, 2, 3, 4]))  # 0
    print(init.minimumSwaps([9]))  # 0
