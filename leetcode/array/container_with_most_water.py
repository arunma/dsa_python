from typing import List


class ContainerWithMostWater:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        left = 0
        right = N - 1

        max_area = float('-inf')
        while left < right:
            dist = right - left
            height = min(heights[left], heights[right])
            max_area = max(max_area, height * dist)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    init = ContainerWithMostWater()
    print(init.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(init.maxArea([1, 1]))  # 1
