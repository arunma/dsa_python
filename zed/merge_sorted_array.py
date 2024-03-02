from typing import *


class MergeSortedArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = len(nums1) - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                m -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1
            k -= 1

        if n >= 0:
            nums1[:n + 1] = nums2[:n + 1]

        print(nums1)


if __name__ == "__main__":
    init = MergeSortedArray()
    print(init.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))  # [1, 2, 2, 3, 5, 6]
    print(init.merge([1], 1, [], 0))  # [1]
    print(init.merge([0], 0, [1], 1))  # [1]
