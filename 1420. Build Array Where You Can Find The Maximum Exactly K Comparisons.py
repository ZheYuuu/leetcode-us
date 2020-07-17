class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
        mod = 10**9+7
        # dp[i][j][k]: # of ways to construct len i array with j as maximum at cost of k
        for j in range(1, m+1):
            dp[1][j][1] = 1
        for a in range(1, n+1):
            for b in range(1, m+1):
                for c in range(1, k+1):
                    ways = 0
                    ways = (ways + b*dp[a-1][b][c])%mod
                    for x in range(1, b):
                        ways = (ways + dp[a-1][x][c-1])%mod
                    dp[a][b][c] = (dp[a][b][c]+ways)%mod
        ans = 0
        for j in range(1, m+1):
            ans  = (ans + dp[n][j][k])%mod
        return ans 