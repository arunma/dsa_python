from typing import *


class NextGreaterElementIi:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [-1] * N
        stack = []
        for i in list(range(N)) * 2:
            num = nums[i]
            while stack and num > nums[stack[-1]]:
                ii = stack.pop()
                result[ii] = nums[i]
            stack.append(i)
        return result


if __name__ == '__main__':
    init = NextGreaterElementIi()
    print(init.nextGreaterElements([1, 2, 1]))  # [2,-1,2]
    print(init.nextGreaterElements([2, 1, 3, 1]))  # [3,3,-1,2]
    print(init.nextGreaterElements([1, 2, 3, 4, 3]))  # [2,3,4,-1,4]
