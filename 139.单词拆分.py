#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(0, i):
                dp[i] = (dp[j] and s[j:i] in wordDict) or dp[i]
                if dp[i]:
                    break
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    data = [
        ("applepenapple", ["apple", "pen"]),
        ("leetcode", ["leet", "code"]),
        ("catsandog",["cats","dog","and","sand","cat"])]
    for d in data:
        t = sol.wordBreak(*d)
        print(t)

# @lc code=end

