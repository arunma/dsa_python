from typing import *


class ValidSudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R = len(board)
        C = len(board[0])
        pairs = []
        for r in range(R):
            for c in range(C):
                tt_row = r // 3
                tt_col = c // 3
                val = board[r][c]
                if val == ".":
                    continue
                pairs.append((val, 'r', r))
                pairs.append((val, 'c', c))
                pairs.append((val, 'tt', tt_row, tt_col))
        return len(pairs) == len(set(pairs))


if __name__ == '__main__':
    init = ValidSudoku()
    sudoku1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    sudoku2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    print(init.isValidSudoku(sudoku1))  # True
    print(init.isValidSudoku(sudoku2))  # False
