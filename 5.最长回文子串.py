#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s):
        if not s:
            return s
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = s[0] 
        for i in range(n):
            dp[i][i] = True
            if i<n-1:
                dp[i][i+1] = s[i]==s[i+1]
                if dp[i][i+1]==True:
                    res = s[i:i+2]
        for i in reversed(range(n-2)):
            for j in range(i+2,n):
                dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
                if dp[i][j] and j-i+1>len(res):
                    res = s[i:j+1]
        return res
        
    # # wrong
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     if not s:
    #         return ''
    #     if len(set(s))==1:
    #         return s
    #     dp = [[False for _ in s] for _ in s]
    #     for i in range(len(s)):
    #         dp[i][i] = True
    #     ret = (0,0)
    #     for j in range(0,n):
    #         for i in range(0,j):
    #             if dp[i][j-1] == True and i-1>=0:
    #                 if len(set(s[i:j]))==1 and s[i]==s[j]:
    #                     dp[i][j]=True
    #                 else:
    #                     dp[i][j] = False 
    #             if dp[i][j-1] == False or i==j-1:
    #                 if i==j-1:
    #                     dp[i][j] = s[i]==s[j]
    #                 else:
    #                     dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
    #             if dp[i][j] and (ret[1]-ret[0])<j-i:
    #                 ret = (i,j)
    #     return s[ret[0]:ret[1]+1]

    # # right
    # def longestPalindrome(self, s):
    #     n = len(s)
    #     if n<=1:
    #         return s
    #     dp = [[False for _ in range(n)] for _ in range(n)]
    #     idx = (0,0)
    #     for i in range(n):
    #         dp[i][i] = True
    #     for j in range(n):
    #         for i in range(0, j):
    #             if s[i] != s[j]:
    #                 continue
    #             if j-i+1<=3:
    #                 dp[i][j] = True
    #             else:
    #                 dp[i][j] = dp[i+1][j-1]
    #             if dp[i][j] and j-i>idx[1]-idx[0]:
    #                 idx = (i,j)
    #     return s[idx[0]:idx[1]+1]
                    
        
# if __name__ == "__main__":
#     sol = Solution()
#     s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#     t = sol.longestPalindrome(s)
#     print(s)

        
# @lc code=end

