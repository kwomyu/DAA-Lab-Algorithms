#Subset Sum (Equal Partition)
def subset(arr):

    s = sum(arr)

    if s % 2:

        return False

    target = s // 2

    dp = [False] * (target + 1)

    dp[0] = True

    for num in arr:

        for j in range(target, num - 1, -1):

            dp[j] = dp[j] or dp[j - num]

    return dp[target]

How it works: Checks if array can be split into two equal-sum subsets using 1D DP. Time: O(n × target) · Space: O(target)
