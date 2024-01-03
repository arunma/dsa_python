from typing import *


class ValidSudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R = len(board)
        C = len(board[0])

        rows = [set() for _ in range(R)]
        cols = [set() for _ in range(C)]
        boxes = [set() for _ in range(R)]

        for r in range(R):
            for c in range(C):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r]:
                    return False
                rows[r].add(val)
                if val in cols[c]:
                    return False
                cols[c].add(val)
                box = (r // 3) * 3 + (c // 3)
                if val in boxes[box]:
                    return False
                boxes[box].add(val)
        return True


if __name__ == '__main__':
    init = ValidSudoku()
    print(init.isValidSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."],
                                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))  # True
    print(init.isValidSudoku(board=[["8", "3", ".", ".", "7", ".", ".", ".", "."],
                                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))  # False
