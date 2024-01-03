# from typing import *
from typing import List


class TrappingRainWater:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0
        left = 0
        right = len(height) - 1
        while height[left] == 0:
            left += 1
        while height[right] == 0:
            right -= 1

        max_left = height[left]
        max_right = height[right]

        trap_water = 0
        while left < right:
            max_left = max(max_left, height[left])
            trap_water += max_left - height[left]

            max_right = max(max_right, height[right])
            trap_water += max_right - height[right]

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return trap_water


if __name__ == '__main__':
    init = TrappingRainWater()
    print(init.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(init.trap(height=[4, 2, 0, 3, 2, 5]))  # 9
    print(init.trap(height=[4, 2, 3]))  # 1
