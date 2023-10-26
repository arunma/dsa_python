from typing import *

class RemoveElement:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        for j, num in enumerate(nums):
            if num !=val:
                nums[c]=num
                c+=1
        return c






if __name__ == '__main__':
    init = RemoveElement()
    init.removeElement(nums = [3,2,2,3], val = 3) # 2, nums = [2,2,_,_]
    init.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2) #5, nums = [0,1,4,0,3,_,_,_]
