from typing import *


class LargestConsecutiveSequence:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        max_length = 0
        for num in nums:
            if num - 1 not in seen:
                incr = 1
                while num + incr in seen:
                    incr += 1
                max_length = max(max_length, incr)
        return max_length


if __name__ == '__main__':
    init = LargestConsecutiveSequence()
    print(init.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))  # 4
    print(init.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
