from typing import *


class Dividearrayintoarrayswithmaxdifference:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        # print(nums)
        N = len(nums)
        result = []
        # lasts = set()
        # firsts = set()
        for i in range(0, len(nums), 3):
            # lasts.add(nums[i + 2])
            # firsts.add(nums[i])
            if i + 2 < N and nums[i + 2] - nums[i] <= k:
                result.append(nums[i:i + 3])
            else:
                return []
        return result


if __name__ == '__main__':
    init = Dividearrayintoarrayswithmaxdifference()
    print(init.divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2))
    print(init.divideArray(nums=[1, 3, 3, 2, 7, 3], k=3))
    print(init.divideArray(nums=[6, 10, 5, 12, 7, 11, 6, 6, 12, 12, 11, 7], k=2))  # [[5,6,6],[6,7,7],[10,11,11],[12,12,12]]
    print(init.divideArray(nums=[15, 13, 12, 13, 12, 14, 12, 2, 3, 13, 12, 14, 14, 13, 5, 12, 12, 2, 13, 2, 2], k=2))
