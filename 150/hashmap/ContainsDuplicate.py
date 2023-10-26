from typing import *


class ContainsDuplicate:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}

        for i, num in enumerate(nums):
            if num in map and abs(map[num] - i) <= k:
                return True
            else:
                map[num] = i
        return False


if __name__ == '__main__':
    init = ContainsDuplicate()
    print(init.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))  # true
    print(init.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))  # true
    print(init.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))  # false
