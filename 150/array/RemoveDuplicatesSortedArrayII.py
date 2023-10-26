from typing import *


class RemoveDuplicatesInSortedArrayII:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=2

        for fast in range(2, len(nums)):
            if nums[slow-2] != nums[fast]:
                nums[slow]=nums[fast]
                slow+=1
        return slow





if __name__ == '__main__':
    init = RemoveDuplicatesInSortedArrayII()
    print(init.removeDuplicates([1,1,1,2,2,3])) #5
    print(init.removeDuplicates([0,0,1,1,1,1,2,3,3])) #7
