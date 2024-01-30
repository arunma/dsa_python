from functools import lru_cache


class OutOfBoundaryPaths:
    def findPaths(self, m: int, n: int, move: int, r: int, c: int) -> int:
        memo = {}
        return self.dfs(m, n, move, r, c, memo)

    def dfs(self, m, n, move, r, c, memo):
        # print(f"r: {r}, c: {c}, move: {move}")
        if (r, c, move) in memo:
            return memo[(r, c, move)]
        if move < 0:
            return 0
        if r < 0 or r > m - 1 or c < 0 or c > n - 1:
            return 1

        count = 0
        neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for nr, nc in neis:
            count += self.dfs(m, n, move - 1, nr, nc, memo)
        memo[(r, c, move)] = count % (10 ** 9 + 7)
        return memo[(r, c, move)]

    def findPaths(self, m: int, n: int, move: int, r: int, c: int) -> int:
        return self.dfs(m, n, move, r, c)

    @lru_cache(None)
    def dfs(self, m, n, move, r, c):
        # print(f"r: {r}, c: {c}, move: {move}")
        if move < 0:
            return 0
        if r < 0 or r > m - 1 or c < 0 or c > n - 1:
            return 1

        count = 0
        neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for nr, nc in neis:
            count += self.dfs(m, n, move - 1, nr, nc)
        return count % (10 ** 9 + 7)


if __name__ == '__main__':
    init = OutOfBoundaryPaths()
    print(init.findPaths(2, 2, 2, 0, 0))  # 6
    # print(init.findPaths(1, 3, 3, 0, 1))  # 12
