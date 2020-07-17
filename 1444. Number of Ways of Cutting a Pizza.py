class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod =  1e9+7
        if not pizza or not pizza[0]:
            return 0
        m = len(pizza)
        n = len(pizza[0])
        dp = [[[0 for _ in range(k+1)] for _ in range(n+1)] for _ in range(m+1)]
        presum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                t = 1 if pizza[i][j] == 'A' else 0
                presum[i][j] = presum[i+1][j]+presum[i][j+1]-presum[i+1][j+1]+t
        for i in range(m):
            for j in range(n):
                    dp[i][j][1] = 1 if presum[i][j]>0 else 0
        for i in reversed(range(m)):    
            for j in reversed(range(n)):
                for p in range(2, k+1):
                    for a in range(i+1, m):
                        if self.valid(presum, i,j, a, j):
                            dp[i][j][p] += dp[a][j][p-1]
                            dp[i][j][p] = dp[i][j][p]%mod
                    for b in range(j+1, n):
                        if self.valid(presum, i,j, i, b):
                            dp[i][j][p] += dp[i][b][p-1]
                            dp[i][j][p] = dp[i][j][p]%mod
        return int(dp[0][0][k])
    
    def valid(self, presum, r1,c1, r2,c2):
        tmp = presum[r1][c1]-presum[r2][c2]
        return tmp>0