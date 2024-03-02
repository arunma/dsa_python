from typing import *


class CoinChange:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for amt in range(amount + 1):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt - coin] + 1, dp[amt])
        return dp[-1] if dp[-1] < float('inf') else -1


if __name__ == "__main__":
    init = CoinChange()
    print(init.coinChange([1, 2, 5], 11))  # 3
    print(init.coinChange([2], 3))  # -1
    print(init.coinChange([1], 0))  # 0
