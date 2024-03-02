from typing import List
class MergeSortedArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1
        j=n-1
        k=len(nums1)-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1

        if j>=0:
            nums1[:j+1]=nums2[:j+1]






if __name__ == '__main__':
    init = MergeSortedArray()
    print(init.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)) #[1,2,2,3,5,6]