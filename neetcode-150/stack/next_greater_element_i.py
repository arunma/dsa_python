from typing import *


# monotonic stack
class NextGreaterElementI:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp = {}
        for num in nums1:
            mapp[num] = -1

        stack = []
        for i, num in enumerate(nums2):
            while stack and num > nums2[stack[-1]]:
                ii = stack.pop()
                if nums2[ii] in mapp:
                    mapp[nums2[ii]] = nums2[i]
            stack.append(i)

        return [mapp[num] for num in nums1]


if __name__ == '__main__':
    init = NextGreaterElementI()
    print(init.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))  # [-1,3,-1]
    print(init.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))  # [3,-1]
