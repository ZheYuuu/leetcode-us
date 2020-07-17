#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == "0":
            return 0
        if n == 1:
            return 1
        dp = [0 for _ in range(n)]
        dp[0] = 1
        if int(s[:2])>26 and s[1]=="0":
            return 0
        else:
            dp[1] = 2 if int(s[:2]) <= 26 and s[1] != "0" else 1
        
        for i in range(2, n):
            if s[i] == "0":
                if int(s[i - 1]) > 2 or s[i-1]=="0":
                    return 0
                dp[i] = dp[i - 2]
            else:
                dp[i] = max(
                    dp[i - 1],
                    dp[i - 1] + dp[i - 2]
                    if (s[i - 1] != "0" and int(s[i - 1 : i + 1]) <= 26)
                    else float("-inf"),
                )
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()

    t = sol.numDecodings("2011")
    print(t)


# @lc code=end

