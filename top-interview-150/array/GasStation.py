from typing import *


class GasStation:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        diffs = [0] * N

        summ = 0
        for i in range(N):
            diffs[i] = gas[i] - cost[i]
            summ += diffs[i]
        if summ < 0:
            return -1

        cumdiff = 0
        max_index = 0
        for i, diff in enumerate(diffs):
            cumdiff += diff
            if cumdiff < 0:
                max_index = i + 1
                cumdiff = 0
        return max_index


if __name__ == '__main__':
    init = GasStation()
    # print(init.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))  # 3
    # print(init.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))  # 3
    print(init.canCompleteCircuit(gas=[3, 1, 1], cost=[1, 2, 2]))  # 0
