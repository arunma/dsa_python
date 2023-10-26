from collections import defaultdict
from typing import *


class MajorityElement:
    # def majorityElement(self, nums: List[int]) -> int:
    #     N=len(nums)
    #     map = defaultdict(int)
    #     for num in nums:
    #         map[num]+=1
    #
    #     for num,counts in map.items():
    #         if counts>N//2:
    #             return num
    #     return -1

    def majorityElement(self, nums: List[int]) -> int:
        N=len(nums)
        count=1
        candidate = nums[0]

        for num in nums[1:]:
            if num == candidate:
                count+=1
            else:
                count -= 1
                if count==0:
                    candidate=num
                    count+=1
        return candidate




if __name__ == '__main__':
    init = MajorityElement()
    print(init.majorityElement([3,3,4]))  # 3
    print(init.majorityElement([6,5,5]))  # 5
    print(init.majorityElement([2,2,1,1,1,2,2])) #2
