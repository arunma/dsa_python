from typing import *


class CanJump:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True

    def canJump(self, nums: List[int]) -> bool:
        return self.can_jump(nums, 0, 0)

    def can_jump(self, nums, i, max_reach):
        if i >= len(nums):
            return True

        if max_reach < i:
            return False

        max_reach = max(i + nums[i], max_reach)
        return self.can_jump(nums, i + 1, max_reach)


if __name__ == "__main__":
    init = CanJump()
    print(init.canJump([2, 3, 1, 1, 4]))  # True
    print(init.canJump([3, 2, 1, 0, 4]))  # False
    print(init.canJump([0, 1]))  # False
