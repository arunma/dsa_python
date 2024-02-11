class UniquePaths:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.unique_paths(m, n, 0, 0, {})

    def unique_paths(self, m, n, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == m - 1 and j == n - 1:
            return 1

        if i == m or j == n:
            return 0

        counts = self.unique_paths(m, n, i + 1, j, memo) + self.unique_paths(m, n, i, j + 1, memo)
        memo[(i, j)] = counts
        return counts
