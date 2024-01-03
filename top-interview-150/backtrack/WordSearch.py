from typing import *


class WordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    seen = set()
                    if self.backtrack(board, word, R, C, r, c, 1, seen):
                        return True
        return False

    def backtrack(self, board, word, R, C, r, c, index, seen):
        if index == len(word):
            return True

        seen.add((r, c))
        pairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for nr, nc in pairs:
            if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen and word[index] == board[nr][nc]:
                if self.backtrack(board, word, R, C, nr, nc, index + 1, seen):
                    return True
        seen.remove((r, c))
        return False


if __name__ == '__main__':
    init = WordSearch()
    print(init.exist(board=[["A", "B", "C", "E"],
                            ["S", "F", "C", "S"],
                            ["A", "D", "E", "E"]], word="ABCCED"))  # True
    print(init.exist(board=[["A", "B", "C", "E"],
                            ["S", "F", "C", "S"],
                            ["A", "D", "E", "E"]], word="SEE"))  # True
    print(init.exist(board=[["A", "B", "C", "E"],
                            ["S", "F", "C", "S"],
                            ["A", "D", "E", "E"]], word="ABCB"))  # False
    print(init.exist(board=[["a", "b"],
                            ["c", "d"]], word="abcd"))  # False

    print(init.exist(board=[["a", "a"]], word="aaa"))  # False
