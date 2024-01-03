from typing import *


class GameOfLife:
    # def gameOfLife(self, board: List[List[int]]) -> None:
    #     R = len(board)
    #     C = len(board[0])
    #
    #     # 0 0 -> 0
    #     # 1 0 -> 1
    #     # 0 1 -> 2
    #     # 1 1 -> 3
    #
    #     for r in range(R):
    #         for c in range(C):
    #             neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r - 1, c - 1), (r + 1, c + 1), (r - 1, c + 1), (r + 1, c - 1)]
    #             count = 0
    #             for nr, nc in neis:
    #                 if -1 < nr < R and -1 < nc < C and board[nr][nc] in [1, 3]:
    #                     count += 1
    #             # if board[r][c] == 1 and count < 2:
    #             #     board[r][c] = 1
    #             # if board[r][c] == 1 and count > 3:
    #             #     board[r][c] = 1  # die
    #             if board[r][c] == 1 and count in [2, 3]:
    #                 board[r][c] = 3
    #             elif board[r][c] == 0 and count == 3:
    #                 board[r][c] = 2
    #
    #     for r in range(R):
    #         for c in range(C):
    #             if board[r][c] == 1:
    #                 board[r][c] = 0
    #             elif board[r][c] in [2, 3]:
    #                 board[r][c] = 1
    #     print(board)

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R = len(board)
        C = len(board[0])

        # if 1 is going to die -1
        # if 0 is going to live 2

        for r in range(R):
            for c in range(C):
                neis = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c + 1), (r + 1, c - 1)]
                count = 0
                for nr, nc in neis:
                    if -1 < nr < R and -1 < nc < C:
                        if board[nr][nc] == 1 or board[nr][nc] == -1:
                            count += 1

                if board[r][c] == 1 and (count < 2 or count > 3):
                    board[r][c] = -1
                elif board[r][c] == 0 and count == 3:
                    board[r][c] = 2

        for r in range(R):
            for c in range(C):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1


if __name__ == '__main__':
    init = GameOfLife()
    print(init.gameOfLife(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))  # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    # print(init.gameOfLife(board=[[1, 1], [1, 0]]))  # [[1,1],[1,1]]
    # print(init.gameOfLife(board=[[0]]))  # [[0]]
    # print(init.gameOfLife(board=[[1]]))  # [[0]]
