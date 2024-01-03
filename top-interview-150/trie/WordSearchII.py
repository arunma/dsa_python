from typing import *


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word):
        node = self
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.end = True


class WordSearchII:
    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     if not board or not words:
    #         return None
    #
    #     R = len(board)
    #     C = len(board[0])
    #
    #     result = []
    #
    #     for r in range(R):
    #         for c in range(C):
    #             for word in words:
    #                 seen = set()
    #                 if (r, c) not in seen and word.startswith(board[r][c]):
    #                     seen.add((r, c))
    #                     if self.dfs(board, r, c, R, C, word[1:], seen):
    #                         result.append(word)
    #                         words.remove(word)
    #
    #     return result
    #
    # def dfs(self, board, r, c, R, C, word, seen):
    #     if not word:
    #         return True
    #     pairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    #     for nr, nc in pairs:
    #         if -1 < nr < R and -1 < nc < C and board[nr][nc] == word[0] and (nr, nc) not in seen:
    #             seen.add((nr, nc))
    #             if self.dfs(board, nr, nc, R, C, word[1:], seen):
    #                 return True
    #     return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R = len(board)
        C = len(board[0])

        root = TrieNode()
        for word in words:
            root.add(word)

        result = set()
        seen = set()

        for r in range(R):
            for c in range(C):
                if board[r][c] in root.children:
                    self.dfs(board, r, c, R, C, result, seen, root.children[board[r][c]], board[r][c])

        return result

    def dfs(self, board, r, c, R, C, result, seen, node, word):
        seen.add((r, c))
        # node = node.children[board[r][c]]
        # word += board[r][c]
        if node.end:
            result.add(word)

        pairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for rr, cc in pairs:
            if -1 < rr < R and -1 < cc < C and board[rr][cc] in node.children and (rr, cc) not in seen:
                self.dfs(board, rr, cc, R, C, result, seen, node.children[board[rr][cc]], word + board[rr][cc])

        seen.remove((r, c))


if __name__ == '__main__':
    init = WordSearchII()
    print(init.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                         words=["oath", "pea", "eat", "rain"]))  # ["eat","oath"]
    print(init.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))  # []
    print(init.findWords(board=[["a", "a"]], words=["aaa"]))
