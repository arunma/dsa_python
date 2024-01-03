from typing import *


class IntersectionOfTwoArrays:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        left = 0
        right = 0

        result = []

        while left < len(nums1) and right < len(nums2):
            print(nums1[left], nums2[right])
            if nums1[left] == nums2[right]:
                if not result or result[-1] != nums1[left]:
                    result.append(nums1[left])
                left += 1
                right += 1
            elif nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1
        return result


if __name__ == '__main__':
    init = IntersectionOfTwoArrays()
    # print(init.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))  # [2]
    print(init.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))  # [9,4]
