from typing import *


class RemoveElement2:
    def removeElement(self, nums: List[int], val: int) -> int:
        r=len(nums)-1
        l=0

        while l<=r:
            if nums[l]==val:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
            else:
                l+=1
        return l





if __name__ == '__main__':
    init = RemoveElement2()
    init.removeElement(nums=[3, 2, 2, 3], val=3)  # 2, nums = [2,2,_,_]
    init.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)  # 5, nums = [0,1,4,0,3,_,_,_]
