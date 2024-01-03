from typing import *


class SingleNumber:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == '__main__':
    init = SingleNumber()
    print(init.singleNumber([2, 2, 1]))  # 1
    print(init.singleNumber([4, 1, 2, 1, 2]))  # 4
    print(init.singleNumber([1]))  # 1
