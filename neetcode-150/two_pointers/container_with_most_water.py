from typing import *


class ContainerWithMostWater:
    def maxArea(self, height: List[int]) -> int:
        max_area = float('-inf')
        left = 0
        right = len(height) - 1
        while left < right:
            dist = right - left
            curr_area = min(height[left], height[right]) * dist
            max_area = max(max_area, curr_area)
            # print(f"left: {left}, right: {right}, dist: {dist}, curr_area: {curr_area}, max_area: {max_area}")
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    init = ContainerWithMostWater()
    print(init.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(init.maxArea(height=[1, 1]))  # 1
