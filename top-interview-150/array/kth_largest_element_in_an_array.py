import heapq
from typing import *


class KthLargestElementInAnArray:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, num)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        N = len(nums)
        return self.quick_select(nums, 0, N - 1, N - k)

    def quick_select(self, nums, low, high, k):
        if low <= high:
            part = self.partition(nums, low, high)
            if part == k:
                return nums[part]
            elif part < k:
                part += 1
                while part < k and nums[part] == nums[part - 1]:
                    part += 1
                return self.quick_select(nums, part, high, k)
            else:
                part -= 1
                while part > k and nums[part] == nums[part + 1]:
                    part -= 1
                return self.quick_select(nums, low, part, k)

    def partition(self, nums, low, high):
        pivot = high
        low_pos = low
        for i in range(low, high):
            if nums[i] <= nums[pivot]:
                nums[low_pos], nums[i] = nums[i], nums[low_pos]
                low_pos += 1
        nums[low_pos], nums[pivot] = nums[pivot], nums[low_pos]
        return low_pos


if __name__ == '__main__':
    init = KthLargestElementInAnArray()
    print(init.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))  # 5
    print(init.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))  # 4
