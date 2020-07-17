#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    # def isMatch(self, s: str, p: str) -> bool:
    #     # Generate Patterns.
    #     pattern = []
    #     for i in range(len(p)):
    #         if p[i] != "*":
    #             if i == len(p) - 1 or p[i + 1] != "*":
    #                 pattern.append((p[i], "#"))
    #             else:
    #                 pattern.append((p[i], "*"))
    #         else:
    #             if i < len(p) - 1 and p[i + 1] == "*":
    #                 return False

    #     self.flag = False

    #     def dfs(s, pattern):
    #         if self.flag:
    #             return True
    #         if not s:
    #             if not pattern:
    #                 self.flag = True
    #             elif pattern[0][1] == "*":
    #                 self.flag = dfs(s[:], pattern[1:])
    #             else:
    #                 self.flag = False
    #             return self.flag
    #         if not pattern:
    #             return False
    #         pt, sign = pattern[0]
    #         flag = False
    #         if pt == ".":
    #             if sign == "*":
    #                 for i in range(len(s) + 1):
    #                     flag = flag or dfs(s[i:], pattern[1:])
    #             else:
    #                 flag = flag or dfs(s[1:], pattern[1:])
    #         else:
    #             if s[0] != pt and sign != "*":
    #                 flag = False
    #             else:
    #                 if sign == "*":
    #                     for i in range(len(s) + 1):
    #                         if i == 1:
    #                             print(s)
    #                         if i == 0:
    #                             flag = flag or dfs(s[:], pattern[1:])
    #                         else:
    #                             if s[i - 1] != pt:
    #                                 break
    #                             flag = flag or dfs(s[i:], pattern[1:])
    #                 else:
    #                     flag = flag or dfs(s[1:], pattern[1:])
    #         return flag

    #     return dfs(s, pattern)

    # def isMatch(self, s: str, p: str) -> bool:
    #     n = len(s)
    #     m = len(p)
    #     dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    #     dp[0][0] = True
    #     # Update the corner case of when s is an empty string but p is not.
    #     for j in range(1, m + 1):
    #         if p[j - 1] == "*":
    #             dp[0][j] = dp[0][j - 2]

    #     for i in range(1, n + 1):
    #         for j in range(1, m + 1):
    #             if s[i - 1] == p[j - 1] or p[j - 1] == ".":
    #                 dp[i][j] = dp[i - 1][j - 1]
    #             elif p[j - 1] == "*":
    #                 a = b = False
    #                 # 0 occurence
    #                 a = dp[i][j - 2]
    #                 # >=1 occurences
    #                 if p[j - 1 - 1] == s[i - 1] or p[j - 1 - 1] == ".":
    #                     b = dp[i - 1][j]
    #                 dp[i][j] = a or b
    #             else:
    #                 dp[i][j] == False
    #     return dp[-1][-1]

    # def isMatch(self, s: str, p: str) -> bool:
    #     n = len(s)
    #     m = len(p)
    #     def helper(s, p, i, j):
    #         if j == m:
    #             return i == n
    #         if j<m-1 and p[j + 1] == "*":
    #             if helper(s, p, i, j + 2):
    #                 return True
    #             while i < n and (s[i] == p[j] or p[j] == "."):
    #                 if helper(s, p, i + 1, j + 2):
    #                     return True
    #                 i = i + 1
    #         elif i < n and (s[i] == p[j] or p[j] == "."):
    #             if helper(s, p, i + 1, j + 1):
    #                 return True
    #         return False

    #     return helper(s, p, 0, 0)
    
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[None for _ in range(m+1)] for _ in range(n+1)]
        def helper(s, p, i, j):
            if dp[i][j]!=None:
                return dp[i][j]
            if j == m:
                dp[i][j] = i == n
                return dp[i][j]
            if j<m-1 and p[j + 1] == "*":
                if helper(s, p, i, j + 2):
                    dp[i][j] = True
                    return True
                if i<n and (p[j]==s[i] or p[j]==".") and helper(s, p, i+1, j):
                    dp[i][j] = True
                    return True
            elif i < n and (s[i] == p[j] or p[j] == "."):
                if helper(s, p, i + 1, j + 1):
                    dp[i][j] = True
                    return True
            dp[i][j] = False
            return False 
        return helper(s, p, 0, 0)
    
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)
        dp = [[False for _ in range(m+1)] for _ in range(n+1)]
        dp[n][m]=True
        for i in reversed(range(n+1)):
            for j in reversed(range(m)):
                if j<m-1 and p[j+1]=="*":
                    dp[i][j] = dp[i][j+2] or i<n and (s[i]==p[j] or p[j]==".") and dp[i+1][j]
                else:
                    dp[i][j] = i<n and (s[i]==p[j] or p[j]==".") and dp[i+1][j+1]
        return dp[0][0]



# if __name__ == "__main__":
#     t = Solution().isMatch("mississippi", "mis*is*ip*.")
#     t = Solution().isMatch("aa", "a")
#     print(t)


# @lc code=end

