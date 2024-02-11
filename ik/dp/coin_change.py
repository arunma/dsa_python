from typing import List


class CoinChange:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     dp = [False] * (amount + 1)
    #     dp[0] = True
    #     for amt in range(amount + 1):
    #         for coin in coins:
    #             if amt > coin and amt + coin < len(dp):
    #                 dp[amt + coin] = True
    #     return dp[-1]

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for amt in range(amount + 1):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])

        return dp[-1] if dp[-1] < float('inf') else -1


if __name__ == '__main__':
    init = CoinChange()
    print(init.coinChange(coins=[1, 2, 5], amount=11))  # 3
    print(init.coinChange(coins=[2], amount=3))  # -1
    print(init.coinChange(coins=[1], amount=0))  # 0
