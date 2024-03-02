from typing import *


class Median_of_two_sorted_arrays:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(B) < len(A):
            A, B = B, A

        N1 = len(A)
        N2 = len(B)

        left = 0
        right = N1
        half = (N1 + N2 + 1) // 2
        while left <= right:
            i = (left + right) // 2
            j = half - i

            aleft = A[i - 1] if i - 1 >= 0 else float('-inf')
            aright = A[i] if i < N1 else float('inf')
            bleft = B[j - 1] if j - 1 >= 0 else float('-inf')
            bright = B[j] if j < N2 else float('inf')

            if aleft <= bright and bleft <= aright:
                if (N1 + N2) & 1:
                    return max(aleft, bleft)
                else:
                    return (max(aleft, bleft) + min(aright, bright)) / 2.0
            elif aleft > bright:
                right = i - 1
            else:
                left = i + 1
        return -1


if __name__ == "__main__":
    init = Median_of_two_sorted_arrays()
    # print(init.findMedianSortedArrays([1, 3], [2]))  # 2.0
    # print(init.findMedianSortedArrays([1, 2], [3, 4]))  # 2.5
    print(init.findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5]))  # 4
