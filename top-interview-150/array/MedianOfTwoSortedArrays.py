from typing import *


class MedianOfTwoSortedArrays:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1 = len(nums1)
        N2 = len(nums2)

        if N1 > N2:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = N1

        while low <= high:
            mx = low + (high - low) // 2
            my = (N1 + N2 + 1) // 2 - mx

            max_left_x = float('-inf') if mx == 0 else nums1[mx - 1]
            min_right_x = float('inf') if mx == N1 else nums1[mx]

            max_left_y = float('-inf') if my == 0 else nums2[my - 1]
            min_right_y = float('inf') if my == N2 else nums2[my]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (N1 + N2) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                high = mx - 1
            else:
                low = mx + 1
        return -1


if __name__ == '__main__':
    init = MedianOfTwoSortedArrays()
    # print(init.findMedianSortedArrays(nums1=[0, 1, 2, 3, 4, 5, 6], nums2=[1, 6, 7]))  # 3.5
    print(init.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))  # 2.0
    print(init.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))  # 2.5
