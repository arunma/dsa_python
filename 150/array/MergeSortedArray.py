from typing import List


class MergeSortedArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        print(i,j,k)
        while j >= 0:
            print(i,j)
            if i>=0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        print(nums1)


if __name__ == '__main__':
    init = MergeSortedArray()
    init.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
    init.merge(nums1=[1, 2, 4, 5, 6, 0], m=5, nums2=[3], n=1)
    init.merge(nums1=[4, 0, 0, 0, 0, 0], m=1, nums2=[1, 2, 3, 5, 6], n=5)
