from typing import *


class SurroundedRegions:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return None
        R = len(board)
        C = len(board[0])

        for r in range(R):
            if board[r][0] == 'O':
                self.dfs(board, r, 0, R, C)
            if board[r][C - 1] == 'O':
                self.dfs(board, r, C - 1, R, C)

        for c in range(C):
            if board[0][c] == 'O':
                self.dfs(board, 0, c, R, C)
            if board[R - 1][c] == 'O':
                self.dfs(board, R - 1, c, R, C)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'B':
                    board[r][c] = 'O'
        return board

    def dfs(self, board, r, c, R, C):
        if not -1 < r < R or not -1 < c < C or board[r][c] == "X" or board[r][c] == "B":
            return
        board[r][c] = 'B'
        pairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for rr, cc in pairs:
            self.dfs(board, rr, cc, R, C)


if __name__ == '__main__':
    init = SurroundedRegions()
    # print(init.solve(board=[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"],["X", "O", "X", "X"]]))  # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    # print(init.solve(board=[["X"]]))  # [["X"]]
    print(init.solve(board=[["O", "O"], ["O", "O"]]))  # [["O","O"],["O","O"]]
