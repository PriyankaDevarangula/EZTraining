def knapsack_dp(p, w, c):
    n = len(p)
    dp = [[-1 for _ in range(c + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for c in range(c + 1):
        dp[0][c] = 0 
    for i in range(1, n + 1):
        for c in range(1, c + 1):
            if w[i - 1] <= c:
                dp[i][c] = max(dp[i-1][c],p[i-1]+dp[i-1][c-w[i-1]])
            else:
                dp[i][c] = dp[i - 1][c]
    return dp[n][c]
p = [5, 10, 15, 7, 8, 9, 4]
w = [1, 3, 5, 4, 1, 3, 2]
c = 15
max_profit = knapsack_dp(p, w, c)
print("The maximum profit is:", max_profit)
