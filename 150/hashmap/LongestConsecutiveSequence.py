from typing import *


class LongestConsecutiveSequence:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_length = 0

        for num in nums:
            left_inc = 1
            right_inc = 1
            while num - left_inc in seen:
                left_inc += 1
            while num + right_inc in seen:
                right_inc += 1

            max_length = max(max_length, left_inc + right_inc - 1)

        return max_length

    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in seen:
                inc = 1
                while num + inc in seen:
                    inc += 1
                max_length = max(max_length, inc)
        return max_length


if __name__ == '__main__':
    init = LongestConsecutiveSequence()
    print(init.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))  # 4
    print(init.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(init.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 9]))  # 10
