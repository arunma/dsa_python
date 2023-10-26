from typing import *


class TwoSumII_InputArrayIsSorted:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l + 1, r + 1]
            elif curr_sum > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]


if __name__ == '__main__':
    init = TwoSumII_InputArrayIsSorted()
    print(init.twoSum(numbers=[2, 7, 11, 15], target=9))  # [1,2]
    print(init.twoSum(numbers=[2, 3, 4], target=6))  # [1,3]
    print(init.twoSum(numbers=[-1, 0], target=-1))  # [1,2]
