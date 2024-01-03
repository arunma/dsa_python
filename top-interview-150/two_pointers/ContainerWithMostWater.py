import sys
from typing import *


class ContainerWithMostWater:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_area = -sys.maxsize
        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, curr_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                curr_area = (heights[l] - heights[r]) * (r - l)
                r -= 1
        return max_area


if __name__ == '__main__':
    init = ContainerWithMostWater()
    print(init.maxArea(heights=[1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(init.maxArea(heights=[1, 1]))  # 1
