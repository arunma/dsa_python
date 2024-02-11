import sys

MOD = (10 ** 9 + 7)


class KnightDialer:
    def knightDialer(self, n: int) -> int:
        R = 4
        C = 3

        ret_count = 0
        for r in range(R):
            for c in range(C):
                ret_count += self.knight_dialer_inner(n, r, c) % MOD
        return ret_count

    def knight_dialer_inner(self, n, r, c, memo):
        if (n, r, c) in memo:
            return memo[(n, r, c)]

        if (r < 0 or r > 3 or c < 0 or c > 2) or (r == 3 and c != 1):
            return 0
        if n == 1:
            return 1

        total_nums = 0
        total_nums += (
                self.knight_dialer_inner(n - 1, r - 1, c - 2, memo) % MOD +
                self.knight_dialer_inner(n - 1, r + 1, c - 2, memo) % MOD +
                self.knight_dialer_inner(n - 1, r - 1, c + 2, memo) % MOD +
                self.knight_dialer_inner(n - 1, r + 1, c + 2, memo) % MOD +
                self.knight_dialer_inner(n - 1, r - 2, c - 1, memo) % MOD +
                self.knight_dialer_inner(n - 1, r + 2, c - 1, memo) % MOD +
                self.knight_dialer_inner(n - 1, r - 2, c + 1, memo) % MOD +
                self.knight_dialer_inner(n - 1, r + 2, c + 1, memo) % MOD
        )

        memo[(n, r, c)] = total_nums % MOD
        return memo[(n, r, c)]

    # @lru_cache(None)
    # def knight_dialer_inner(self, n, r, c):
    #     if (r < 0 or r > 3 or c < 0 or c > 2) or (r == 3 and c != 1):
    #         return 0
    #     if n == 1:
    #         return 1
    #
    #     total_nums = 0
    #     total_nums += (
    #             self.knight_dialer_inner(n - 1, r - 1, c - 2) % MOD +
    #             self.knight_dialer_inner(n - 1, r + 1, c - 2) % MOD +
    #             self.knight_dialer_inner(n - 1, r - 1, c + 2) % MOD +
    #             self.knight_dialer_inner(n - 1, r + 1, c + 2) % MOD +
    #             self.knight_dialer_inner(n - 1, r - 2, c - 1) % MOD +
    #             self.knight_dialer_inner(n - 1, r + 2, c - 1) % MOD +
    #             self.knight_dialer_inner(n - 1, r - 2, c + 1) % MOD +
    #             self.knight_dialer_inner(n - 1, r + 2, c + 1) % MOD
    #     )
    #
    #     return total_nums % MOD

    def knightDialer(self, n: int) -> int:
        R = 4
        C = 3

        # n+1 * R * C
        dp = [[[0] * 3 for _ in range(R)] for _ in range(n + 1)]
        ret_count = 0
        for r in range(R):
            for c in range(C):
                ret_count = (ret_count + self.knight_dialer_inner(n, r, c, dp)) % MOD
        return ret_count

    def knight_dialer_inner(self, n, r, c, dp):
        if r < 0 or c < 0 or r >= 4 or c >= 3 or (r == 3 and c != 1):
            # if (r < 0 or r > 3 or c < 0 or c > 2) or (r == 3 and c != 1):
            return 0
        if n == 1:
            return 1

        if dp[n][r][c] > 0:
            return dp[n][r][c]

        # dp[n][r][c] = (
        #         self.knight_dialer_inner(n - 1, r - 1, c - 2, dp) % MOD +
        #         self.knight_dialer_inner(n - 1, r + 1, c - 2, dp) % MOD +
        #         self.knight_dialer_inner(n - 1, r - 1, c + 2, dp) % MOD +
        #         self.knight_dialer_inner(n - 1, r + 1, c + 2, dp) % MOD +
        #         self.knight_dialer_inner(n - 1, r - 2, c - 1, dp) % MOD +
        #         self.knight_dialer_inner(n - 1, r + 2, c - 1, dp) % MOD +
        #         self.knight_dialer_inner(n - 1, r - 2, c + 1, dp) % MOD +
        #         self.knight_dialer_inner(n - 1, r + 2, c + 1, dp) % MOD
        # )

        dp[n][r][c] = (
                self.knight_dialer_inner(n - 1, r - 1, c - 2, dp) % MOD +
                self.knight_dialer_inner(n - 1, r - 2, c - 1, dp) % MOD +
                self.knight_dialer_inner(n - 1, r - 2, c + 1, dp) % MOD +

                self.knight_dialer_inner(n - 1, r - 1, c + 2, dp) % MOD +
                self.knight_dialer_inner(n - 1, r + 1, c + 2, dp) % MOD +
                self.knight_dialer_inner(n - 1, r + 2, c + 1, dp) % MOD +
                self.knight_dialer_inner(n - 1, r + 2, c - 1, dp) % MOD +
                self.knight_dialer_inner(n - 1, r + 1, c - 2, dp) % MOD
        )

        return dp[n][r][c] % MOD

    # def knightDialer(self, n):
    #     M = [[[0] * 3 for _ in range(4)] for _ in range(n + 1)]
    #     s = 0
    #
    #     for i in range(4):
    #         for j in range(3):
    #             s = (s + self.knight_dialer_inner(M, i, j, n)) % MOD
    #
    #     return int(s)
    #
    # def knight_dialer_inner(self, M, r, c, n):
    #     if r < 0 or c < 0 or r >= 4 or c >= 3 or (r == 3 and c != 1):
    #         return 0
    #
    #     if n == 1:
    #         return 1
    #
    #     if M[n][r][c] > 0:
    #         return M[n][r][c]
    #
    #     M[n][r][c] = (
    #                          self.knight_dialer_inner(M, r - 1, c - 2, n - 1) % MOD +
    #                          self.knight_dialer_inner(M, r - 2, c - 1, n - 1) % MOD +
    #                          self.knight_dialer_inner(M, r - 2, c + 1, n - 1) % MOD +
    #                          self.knight_dialer_inner(M, r - 1, c + 2, n - 1) % MOD +
    #                          self.knight_dialer_inner(M, r + 1, c + 2, n - 1) % MOD +
    #                          self.knight_dialer_inner(M, r + 2, c + 1, n - 1) % MOD +
    #                          self.knight_dialer_inner(M, r + 2, c - 1, n - 1) % MOD +
    #                          self.knight_dialer_inner(M, r + 1, c - 2, n - 1) % MOD
    #                  ) % MOD
    #
    #     return M[n][r][c]


# paths

if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    init = KnightDialer()
    print(init.knightDialer(1))  # 10
    print(init.knightDialer(2))  # 20
    print(init.knightDialer(3))  # 46
    print(init.knightDialer(3131))  # 136006598
