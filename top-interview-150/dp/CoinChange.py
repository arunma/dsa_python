import sys
from typing import *


class CoinChange:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for amt in range(1, amount + 1):
                if amt >= coin:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)
        return dp[-1] if dp[-1] != sys.maxsize else -1


if __name__ == '__main__':
    init = CoinChange()
    print(init.coinChange(coins=[1, 2, 5], amount=11))  # 3
    print(init.coinChange(coins=[2], amount=3))  # -1
    print(init.coinChange(coins=[1], amount=0))  # 0
    print(init.coinChange(coins=[1], amount=1))  # 1
