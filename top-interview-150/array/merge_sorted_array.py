from typing import *


class MergeSortedArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = len(nums1) - 1
        fi = m - 1
        si = n - 1

        while fi >= 0 and si >= 0:
            if nums1[fi] > nums2[si]:
                nums1[last] = nums1[fi]
                fi -= 1
            else:
                nums1[last] = nums2[si]
                si -= 1
            last -= 1

        if si >= 0:
            nums1[:si + 1] = nums2[:si + 1]

        print(nums1)


if __name__ == '__main__':
    init = MergeSortedArray()
    # print(init.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    print(init.merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5))
