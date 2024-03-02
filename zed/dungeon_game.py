from collections import deque
from typing import *


class DungeonGame:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        R = len(dungeon)
        C = len(dungeon[0])
        
        queue = deque([(0, 0, dungeon[0][0])])

        while queue:
            (r, c, val) = queue.popleft()
            neis = [(r + 1, c), (r, c + 1)]
            for nr, nc in neis:
                if -1<nr<R and -1<nc<C:


if __name__ == "__main__":
    init = DungeonGame()
    print(init.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))  # 7
    print(init.calculateMinimumHP([[0]]))  # 1
