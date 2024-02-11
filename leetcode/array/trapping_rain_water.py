from typing import *


class TrappingRainWater:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        N = len(heights)
        if N == 1:
            return 0

        left = 0
        right = N - 1
        while heights[left] == 0:
            left += 1
        while heights[right] == 0:
            right -= 1
        if left >= right:
            return 0

        max_left = heights[left]
        max_right = heights[right]
        trapped = 0
        while left < right:
            hleft = heights[left]
            hright = heights[right]
            if hleft < hright:
                max_left = max(max_left, hleft)
                trapped += max_left - hleft
                left += 1
            else:
                max_right = max(max_right, hright)
                trapped += max_right - hright
                right -= 1
        return trapped


if __name__ == '__main__':
    init = TrappingRainWater()
    print(init.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(init.trap([4, 2, 0, 3, 2, 5]))  # 9
    print(init.trap([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 0
