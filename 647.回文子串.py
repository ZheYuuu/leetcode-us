#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)        
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = n 
        for i in range(n):
            dp[i][i] = True
            if i<n-1:
                dp[i][i+1] = s[i]==s[i+1]
                res += 1 if dp[i][i+1] else 0
        for j in range(n-2):
            for i in range(n):
                if 2+i+j<n:
                    dp[i][2+i+j] = dp[i+1][2+i+j-1] and s[i]==s[2+i+j]
                    res += 1 if dp[i][2+i+j] else 0
                else:
                    break
        return res
# @lc code=end

