from typing import *


class TrapRainingWater:
    def trap(self, heights: List[int]) -> int:
        N = len(heights)
        trapped = 0
        l = 0
        r = N - 1

        while l < N and heights[l] == 0:
            l += 1
        while r > -1 and heights[r] == 0:
            r -= 1

        if l >= r:
            return 0
        maxleft = heights[l]
        maxright = heights[r]

        while l < r:
            if heights[l] < heights[r]:
                maxleft = max(maxleft, heights[l])
                trapped += maxleft - heights[l]
                l += 1
            else:
                maxright = max(maxright, heights[r])
                trapped += maxright - heights[r]
                r -= 1
        return trapped


if __name__ == '__main__':
    init = TrapRainingWater()
    print(init.trap(heights=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(init.trap(heights=[4, 2, 0, 3, 2, 5]))  # 9
    print(init.trap(heights=[0]))  # 9
