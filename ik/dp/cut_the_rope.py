def max_product_from_cut_pieces(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for size in range(2, n + 1):
        max_product = 0
        for cost in range(1, n):
            curr_prod = cost * dp[size - cost]
            exist_prod = cost * (size - cost)
            max_product = max(max_product, curr_prod, exist_prod)
        dp[size] = max(dp[size], max_product)
    print(dp)
    return dp[-1]


if __name__ == '__main__':
    print(max_product_from_cut_pieces(4))
