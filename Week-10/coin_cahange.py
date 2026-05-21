#Dynamic Programming I
Coin Change (Count Ways)
def coin_change(coins, target):

    dp = [0] * (target + 1)

    dp[0] = 1

    for c in coins:

        for i in range(c, target + 1):

            dp[i] += dp[i - c]

    return dp[target]

How it works: Bottom-up DP; dp[i] stores the number of ways to make amount i. Time: O(n × target) · Space: O(target)
