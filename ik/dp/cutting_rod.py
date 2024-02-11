# def get_maximum_profit(prices):
#     N = len(prices)
#     if N == 0:
#         return 0
#     return get_maximum_profit_inner(prices, 0, N)
#
#
# def get_maximum_profit_inner(prices, profit, N):
#     if N == 0:
#         return profit
#
#     max_profit = float('-inf')
#     for i in range(1, N + 1):
#         prof = get_maximum_profit_inner(prices, profit + prices[i - 1], N - 1)
#         max_profit = max(max_profit, prof)
#     return max_profit

def get_maximum_profit(prices):
    N = len(prices)
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        max_profit = float('-inf')
        for j in range(i):
            max_profit = prices[j] + dp[i - j - 1]
        dp[i] = max_profit
    return dp[-1]


if __name__ == '__main__':
    print(get_maximum_profit([1, 5, 8, 9, 10]))  # 10
    print(get_maximum_profit([1, 5, 8, 9, 10, 17, 17, 20]))  # 22
