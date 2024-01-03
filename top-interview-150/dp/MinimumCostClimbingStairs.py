from typing import *


class MinimumCostClimbingStairs:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        memo[0] = cost[0]
        memo[1] = cost[1]
        min_cost = min(self.min_cost_climbing_stairs(cost, n - 1, memo), self.min_cost_climbing_stairs(cost, n - 2, memo))
        return min_cost

    def min_cost_climbing_stairs(self, cost, i, memo):
        if i < 0:
            return 0

        if i == 0 or i == 1:
            return memo[i]

        if i not in memo:
            one_step = cost[i] + self.min_cost_climbing_stairs(cost, i - 1, memo)
            two_step = cost[i] + self.min_cost_climbing_stairs(cost, i - 2, memo)
            memo[i] = min(one_step, two_step)
        return memo[i]


if __name__ == '__main__':
    init = MinimumCostClimbingStairs()
    print(init.minCostClimbingStairs(cost=[10, 15, 20]))  # 15
    print(init.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
