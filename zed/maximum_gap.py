import math
import sys
from typing import *


class MaximumGap:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        mini = min(nums)
        maxi = max(nums)

        if len(nums) == 2:
            return maxi - mini

        N = len(nums)
        bucket_size = ((maxi - mini) // (N - 1)) + 1
        min_bucket = [sys.maxsize] * N
        max_bucket = [-sys.maxsize] * N

        print(f"bucket: {bucket_size}")
        for num in nums:
            bucket = (num - mini) // bucket_size
            min_bucket[bucket] = min(min_bucket[bucket], num)
            max_bucket[bucket] = max(max_bucket[bucket], num)

        print("minbucket", min_bucket)
        print("maxbucket", max_bucket)
        max_gap = float('-inf')
        prev = max_bucket[0]
        for i in range(1, N):
            if min_bucket[i] == sys.maxsize:
                continue
            max_gap = max(max_gap, min_bucket[i] - prev)
            prev = max_bucket[i]

        return max_gap


if __name__ == "__main__":
    init = MaximumGap()
    print(init.maximumGap([1, 1, 1, 1]))  # 1
    print(init.maximumGap([1, 2]))  # 3
    print(init.maximumGap([100, 3, 2, 1]))  # 3
    print(init.maximumGap([3, 6, 9, 1]))  # 3
    # print(init.maximumGap([10]))  # 0
