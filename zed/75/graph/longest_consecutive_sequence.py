from typing import *


class LongestConsecutiveSequence:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_count = 0
        for num in nums:
            count = 1
            if num - 1 not in nums:
                while num + count in nums:
                    count += 1
                max_count = max(max_count, count)
        return max_count


if __name__ == "__main__":
    init = LongestConsecutiveSequence()
    print(init.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
    print(init.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
