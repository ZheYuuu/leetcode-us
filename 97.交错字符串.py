#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n = len(s1),len(s2)
        if m+n != len(s3):
            return False
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True 
        for i in range(1,m+1):
            
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
        for j in range(1,n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1]==s3[j-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = (dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[-1][-1]



# @lc code=end

