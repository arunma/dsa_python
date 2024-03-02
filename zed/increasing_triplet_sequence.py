import bisect
from typing import *


class IncreasingTripletSequence:
    def increasingTriplet(self, nums: List[int]) -> bool:
        subs = [nums[0]]
        for num in nums:
            if num > subs[-1]:
                subs.append(num)
            else:
                iloc = bisect.bisect_left(subs, num)
                subs[iloc] = num
            if len(subs) == 3:
                return True

        return False


if __name__ == "__main__":
    init = IncreasingTripletSequence()
    print(init.increasingTriplet([1, 2, 3, 4, 5]))  # True
    print(init.increasingTriplet([5, 4, 3, 2, 1]))  # False
    print(init.increasingTriplet([2, 1, 5, 0, 4, 6]))  # True
