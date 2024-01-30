from typing import *


class DailyTemperatures:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        stack = []
        result = [0] * N

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                val, ii = stack.pop()
                result[ii] = i - ii
            stack.append((temp, i))
        return result

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        result = [0] * N
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                ii = stack.pop()
                result[ii] = i - ii
            stack.append(i)

        return result


if __name__ == '__main__':
    init = DailyTemperatures()
    print(init.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]
    print(init.dailyTemperatures(temperatures=[30, 40, 50, 60]))  # [1, 1, 1, 0]
    print(init.dailyTemperatures(temperatures=[30, 60, 90]))  # [1, 1, 0]
