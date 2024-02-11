from typing import List


class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if not nums:
            return 0
        if N == 1:
            return nums[0]
        elif N == 2:
            return max(nums)
        max_rob = float('-inf')
        for i, num in enumerate(nums):

            if i + 2 < N:
                curr_rob = nums[i] + self.rob(nums[i + 2:])
                max_rob = max(max_rob, curr_rob)
            else:
                max_rob = max(max_rob, num)
        return max_rob

    def rob_memo(self, nums: List[int], memo={}) -> int:
        if tuple(nums) in memo:
            return memo[tuple(nums)]
        N = len(nums)
        if not nums:
            return 0
        if N == 1:
            return nums[0]
        elif N == 2:
            return max(nums)
        max_rob = float('-inf')
        for i, num in enumerate(nums):
            if i + 2 < N:
                curr_rob = nums[i] + self.rob(nums[i + 2:])
                max_rob = max(max_rob, curr_rob)
            else:
                max_rob = max(max_rob, num)
        memo[tuple(nums)] = max_rob
        return max_rob

    # Very nice !
    def rob(self, nums: List[int]) -> int:
        return self.rob_inner(nums, len(nums) - 1)

    def rob_inner(self, nums, i):
        if i < 0:
            return 0
        N = len(nums)
        # if N == 1:
        #     return nums[0]
        # elif N == 2:
        #     return max(nums)

        max_rob = max(nums[i] + self.rob_inner(nums, i - 2), self.rob_inner(nums, i - 1))
        return max_rob

    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [float('-inf')] * (N + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, N):
            dp[i + 1] = max(nums[i] + dp[i - 1], dp[i])

        return dp[-1]

    # Wow !
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        prev1 = 0
        prev2 = 0
        for num in nums:
            temp = prev1
            prev1 = max(num + prev2, prev1)
            prev2 = temp

        return prev1


if __name__ == '__main__':
    init = HouseRobber()
    print(init.rob(nums=[1, 2, 3, 1]))  # 4
    print(init.rob(nums=[2, 7, 9, 3, 1]))  # 12
    print(init.rob(nums=[2, 1, 1, 2]))  # 4
    print(init.rob(nums=[1, 3, 1]))  # 4
