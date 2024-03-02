from collections import deque
from typing import *


class RaceCar:
    # def racecar(self, target: int) -> int:
    #     return self.race_car(0, 1, target, 0, {})
    #
    # def race_car(self, position, speed, target, steps, memo):
    #     if (position, speed) in memo:
    #         return memo[(position, speed)]
    #     print(position, target)
    #     if position == target:
    #         return steps
    #     if position > target:
    #         return float('inf')
    #
    #     min_steps = float('inf')
    #     accelerate = self.race_car(position + speed, speed * 2, target, steps + 1, memo)
    #     reverse = self.race_car(position + speed, speed - 1 if speed > 0 else 1, target, steps + 1, memo)
    #     min_steps = min(min_steps, accelerate, reverse)
    #     memo[(position, speed)] = min_steps
    #     return min_steps

    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        while queue:
            pos, speed, dist = queue.popleft()
            if pos == target:
                return dist
            queue.append((pos + speed, speed * 2, dist + 1))
            if speed > 0:
                if pos + speed > target:
                    queue.append((pos, -1, dist + 1))
            else:
                if pos + speed < target:
                    queue.append((pos, 1, dist + 1))

        return -1

    def racecar(self, target):
        queue = deque([(0, 1, 0)])
        while queue:
            pos, speed, dist = queue.popleft()
            if pos == target:
                return dist
            queue.append((pos + speed, speed * 2, dist + 1))
            if speed > 0:
                if pos + speed > target:
                    queue.append((pos, -1, dist + 1))
            else:
                if pos + speed < target:
                    queue.append((pos, 1, dist + 1))


if __name__ == "__main__":
    init = RaceCar()
    print(init.racecar(3))  # 2
    print(init.racecar(6))  # 5
    print(init.racecar(5617))  # 5
