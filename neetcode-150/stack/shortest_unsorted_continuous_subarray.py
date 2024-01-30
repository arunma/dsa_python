from typing import *


class ShortestUnsortedContinuousSubarray:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        N = len(nums)
        left = N
        for i, num in enumerate(nums):
            while stack and num < nums[stack[-1]]:
                ii = stack.pop()
                left = min(left, ii)
            stack.append(i)

        stack = []
        right = 0
        for i in reversed(range(N)):
            num = nums[i]
            while stack and num > nums[stack[-1]]:
                ii = stack.pop()
                right = max(right, ii)
            stack.append(i)

        return (right - left + 1) if right - left > 0 else 0


if __name__ == '__main__':
    init = ShortestUnsortedContinuousSubarray()
    print(init.findUnsortedSubarray(nums=[2, 6, 4, 8, 10, 9, 15]))  # 5
    print(init.findUnsortedSubarray(nums=[1, 2, 3, 4]))  # 0
