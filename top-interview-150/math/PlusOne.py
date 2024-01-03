from typing import *


class PlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        index = len(digits) - 1
        while carry and index >= 0:
            carry, value = divmod(digits[index] + carry, 10)
            digits[index] = value
            index -= 1
        if carry:
            return [carry] + digits
        return digits


if __name__ == '__main__':
    init = PlusOne()
    print(init.plusOne(digits=[1, 2, 3]))  # [1,2,4]
    print(init.plusOne(digits=[4, 3, 2, 1]))  # [4,3,2,2]
    print(init.plusOne(digits=[0]))  # [1]
    print(init.plusOne(digits=[9]))  # [1,0]
