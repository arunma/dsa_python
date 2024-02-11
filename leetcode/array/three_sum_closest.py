from typing import List


class ThreeSumClosest:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if N < 3:
            return -1
        nums.sort()
        closest = sum(nums[:3])
        for i, num in enumerate(nums):
            left = i + 1
            right = N - 1
            while left < right:
                summ = nums[left] + nums[right] + nums[i]
                if summ == target:
                    return summ
                if abs(summ - target) < abs(closest - target):
                    closest = summ
                if summ < target:
                    left += 1
                else:
                    right -= 1
        return closest


if __name__ == '__main__':
    init = ThreeSumClosest()
    print(init.threeSumClosest([-1, 2, 1, -4], 1))  # 2
    print(init.threeSumClosest([0, 0, 0], 1))  # 0
    print(init.threeSumClosest([1, 1, 1, 0], -100))  # 2
