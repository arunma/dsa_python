from typing import *


class Pattern132:
    def find132pattern(self, nums: List[int]) -> bool:
        smallest = float('inf')
        stack = []
        for num in nums:  # decreasing mono stack
            while stack and num >= stack[-1][0]:
                stack.pop()

            if stack and num > stack[-1][1]:
                return True
            stack.append((num, smallest))
            smallest = min(smallest, num)
        return False


if __name__ == '__main__':
    init = Pattern132()
    print(init.find132pattern([1, 2, 3, 4]))  # False
    print(init.find132pattern([3, 1, 4, 2]))  # True
    print(init.find132pattern([-1, 3, 2, 0]))  # True
    print(init.find132pattern([1, 0, 1, -4, -3]))  # False
    print(init.find132pattern([3, 5, 0, 3, 4]))  # True
