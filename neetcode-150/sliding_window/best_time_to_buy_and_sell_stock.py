from typing import *


class BestTimeToBuyAndSellStock:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        low_so_far = prices[0]
        high_so_far = prices[0]
        for price in prices:
            if price < low_so_far:
                low_so_far = price
                high_so_far = price
            if price > high_so_far:
                high_so_far = price

            max_profit = max(max_profit, high_so_far - low_so_far)
        return max_profit


if __name__ == '__main__':
    init = BestTimeToBuyAndSellStock()
    print(init.maxProfit(prices=[7, 1, 5, 3, 6, 4]))  # 5
    print(init.maxProfit(prices=[7, 6, 4, 3, 1]))  # 0
