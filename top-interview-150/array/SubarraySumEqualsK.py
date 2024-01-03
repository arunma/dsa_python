from collections import defaultdict
from typing import *


class SubarraySumEqualsK:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            count += prefix[curr_sum - k]
            prefix[curr_sum] += 1
        return count


if __name__ == '__main__':
    init = SubarraySumEqualsK()
    print(init.subarraySum(nums=[1, 1, 1], k=2))
    print(init.subarraySum(nums=[1, 2, 3], k=3))
