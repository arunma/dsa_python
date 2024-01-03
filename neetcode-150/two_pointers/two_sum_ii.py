from typing import *


class TwoSumII:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left <= right:
            summ = numbers[left] + numbers[right]
            if summ == target:
                return [left + 1, right + 1]
            if summ < target:
                left += 1
            elif summ > target:
                right -= 1
        return [-1, -1]


if __name__ == '__main__':
    init = TwoSumII()
    print(init.twoSum(numbers=[2, 7, 11, 15], target=9))  # [1,2]
    print(init.twoSum(numbers=[2, 3, 4], target=6))  # [1,3]
    print(init.twoSum(numbers=[-1, 0], target=-1))  # [1,2]
