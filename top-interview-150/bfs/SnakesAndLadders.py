from collections import deque
from typing import *


class SnakesAndLadders:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        if not board:
            return 0

        R = len(board)
        C = len(board[0])
        target = R * C

        label = 1
        cols = [c for c in range(C)]
        label_to_rc = {}
        for r in range(R - 1, -1, -1):
            for c in cols:
                label_to_rc[label] = (r, c)
                label += 1
            cols.reverse()

        # print(label_to_rc)
        queue = deque([(1, 0)])  # curr, dist
        seen = set()
        while queue:
            curr, dist = queue.popleft()
            if curr == target:
                return dist
            for nei in range(curr + 1, min(curr + 6, target) + 1):
                if nei not in seen:
                    seen.add(nei)
                    nr, nc = label_to_rc[nei]
                    dest = board[nr][nc] if board[nr][nc] != -1 else nei
                    queue.append((dest, dist + 1))
        return -1


if __name__ == '__main__':
    init = SnakesAndLadders()
    print(init.snakesAndLadders(
        board=[[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1],
               [-1, 15, -1, -1, -1, -1]]))  # 4
    print(init.snakesAndLadders(board=[[-1, -1], [-1, 3]]))  # 1
    print(init.snakesAndLadders(board=[[1, 1, -1], [1, 1, 1], [-1, 1, 1]]))  # -1
    print(init.snakesAndLadders(board=[[-1, -1, -1], [-1, 9, 8], [-1, 8, 9]]))  # 1
    print(init.snakesAndLadders(board=[[-1, 1, 2, -1], [2, 13, 15, -1], [-1, 10, -1, -1], [-1, 6, 2, 8]]))
