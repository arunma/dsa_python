import bisect
from typing import *


class MinimumCostToMakeArrayEqualindromic:
    # def minimumCost(self, nums: List[int]) -> int:
    #     # find average
    #     nums.sort()
    #     # avg = nums[len(nums) // 2]
    #     # cost = 0
    #     # for num in nums:
    #     #     cost += abs(num - avg)
    #     # return cost
    #     summ = sum(nums)
    #     avg = summ // len(nums)
    #     median = nums[len(nums) // 2]
    #     # find average diffence between numbers
    #     diff = 0
    #     for num in nums:
    #         diff += abs(num - avg)
    #     # find median diffence between numbers
    #     diff2 = 0
    #     for num in nums:
    #         diff2 += abs(num - median)
    #
    #     print("summ, avg, median, diff, diff2", summ, avg, median, "-->", diff, diff2)
    #     if diff2 < diff:
    #         return diff2
    #     else:
    #         return diff

    # def minimumCost(self, nums: List[int]) -> int:
    #     # find average
    #     nums.sort()
    #     diff = 0
    #     for i in range(1, len(nums)):
    #         diff += abs(nums[i] - nums[i - 1])
    #
    #     avg_diff = diff // len(nums)
    #     steps = 0
    #     pivot = nums[0] + avg_diff
    #     for i in range(len(nums)):
    #         steps += abs(nums[i] - pivot)
    #
    #     print("avg_diff, pivot, steps", avg_diff, pivot, steps)

    # def minimumCost(self, nums: List[int]) -> int:
    #     nums.sort()
    #     N = len(nums)
    #     median = nums[N // 2]
    #     # M = N // 2
    #     # median = (nums[M - 1] + nums[M]) // 2
    #     cost = 0
    #     for num in nums:
    #         cost += abs(num - median)
    #     return cost

    # def minimumCost(self, nums: List[int]) -> int:
    #     nums.sort()
    #     # start from num at index 0 and increment 1 (try all integers) and end at last num and find the cost of each number to be equal to it
    #     # find the minimum cost
    #     min_cost = float('inf')
    #     for pivot in range(nums[0], nums[-1] + 1):
    #         cost = 0
    #         for num in nums:
    #             cost += abs(num - pivot)
    #         min_cost = min(min_cost, cost)
    #     return min_cost

    def minimumCost(self, nums: List[int]) -> int:

        palindrome = []
        for i in range(1, 10 ** 5 + 3):
            palindrome.append(int(str(i) + str(i)[::-1]))
            palindrome.append(int(str(i) + str(i)[:-1][::-1]))

        palindrome.sort()

        nums.sort()
        n = len(nums)
        med = nums[n // 2]
        p = bisect.bisect_left(palindrome, med)
        mini = nums[0]
        maxi = nums[-1]
        minip = bisect.bisect_left(palindrome, mini)
        maxip = bisect.bisect_right(palindrome, maxi)
        # print("minis", minip, maxip)
        ans = float('inf')
        for p in range(minip, maxip):
            # for i in range(p - 1, p + 3):
            print("palin", palindrome[p])
            ans = min(ans, sum(abs(x - palindrome[i]) for x in nums))
        return ans

    def minimumCost(self, nums: List[int]) -> int:

        palindrome = []
        for i in range(1, 10 ** 5 + 3):
            palindrome.append(int(str(i) + str(i)[::-1]))
            palindrome.append(int(str(i) + str(i)[:-1][::-1]))

        palindrome.sort()
        # nums.sort()
        mini = nums[0]
        maxi = nums[-1]
        minip = bisect.bisect_left(palindrome, mini)
        maxip = bisect.bisect_right(palindrome, maxi)
        ans = float('inf')
        for p in range(minip, maxip):
            ans = min(ans, sum(abs(x - palindrome[p]) for x in nums))
        return ans


if __name__ == '__main__':
    init = MinimumCostToMakeArrayEqualindromic()
    # print(init.minimumCost(nums=[1, 2, 3, 4, 5])) #3
    print(init.minimumCost(nums=[10, 12, 13, 14, 15]))  # 11
    # print(init.minimumCost(nums=[22, 33, 22, 33, 22])) #22
