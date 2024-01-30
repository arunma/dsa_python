from typing import List


class SnakeAndLadders:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        queue = [(1, 0)]  # cell, dist
        R = len(board)
        C = len(board[0])

        grid_to_rc = {}
        label = 1
        cols = [c for c in range(C)]

        for r in range(R - 1, -1, -1):
            for c in cols:
                grid_to_rc[label] = (r, c)
                label += 1
            cols.reverse()

        print(grid_to_rc)

        seen = set()
        while queue:
            curr, dist = queue.pop(0)
            if curr == (R * C):
                return dist

            for nei in range(curr + 1, min(curr + 6, R * C) + 1):
                nr, nc = grid_to_rc[nei]

                if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    dest = board[nr][nc] if board[nr][nc] != -1 else nei
                    queue.append((dest, dist + 1))

        return -1


if __name__ == '__main__':
    init = SnakeAndLadders()
    print(init.snakesAndLadders(
        board=[[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1],
               [-1, 15, -1, -1, -1, -1]]))  # 4
    # print(init.snakesAndLadders(board=[[-1, -1], [-1, 3]]))  # 1
    # print(init.snakesAndLadders(board=[[1, 1, -1], [1, 1, 1], [-1, 1, 1]]))  # -1
    # print(init.snakesAndLadders(board=[[-1, -1, -1], [-1, 9, 8], [-1, 8, 9]]))  # 1
    # print(init.snakesAndLadders(board=[[-1, 1, 2, -1], [2, 13, 15, -1], [-1, 10, -1, -1], [-1, 6, 2, 8]]))
