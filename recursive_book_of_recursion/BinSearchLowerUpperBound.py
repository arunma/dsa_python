class BinSearchLowerUpperBound:
    def lower_bound(self, nums, val):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < val:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def lower_bound(self, nums, val):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= val:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == '__main__':
    init = BinSearchLowerUpperBound()
    print(init.lower_bound([1, 2, 2, 3, 3, 3, 4, 5], 3))
