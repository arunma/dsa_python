from typing import *


class RemoveDuplicates2:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 1

        j=1
        for i in range(1,N):
           if nums[i]!=nums[i-1]:
               nums[j]=nums[i]
               j+=1
        return j




if __name__ == '__main__':
    init = RemoveDuplicates2()
    print(init.removeDuplicates([1,1,2])) #2
    print(init.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) #5
