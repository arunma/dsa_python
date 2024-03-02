from typing import *


class TrappingRainWater:
    def trap(self, heights: List[int]) -> int:
        N = len(heights)
        left = 0
        right = N - 1
        # while heights[left] == 0:
        #     left += 1
        # while heights[right] == 0:
        #     right -= 1

        max_left = heights[left]
        max_right = heights[right]
        trapped_water = 0

        while left < right:
            hleft = heights[left]
            hright = heights[right]
            max_left = max(max_left, hleft)
            max_right = max(max_right, hright)

            trapped_water += max_left - hleft
            trapped_water += max_right - hright

            if hleft < hright:
                left += 1
            else:
                right -= 1
        return trapped_water


if __name__ == "__main__":
    init = TrappingRainWater()
    print(init.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(init.trap([4, 2, 0, 3, 2, 5]))  # 9
