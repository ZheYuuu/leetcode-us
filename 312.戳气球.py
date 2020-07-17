#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
class Solution:
    def maxCoins(self, nums)-> int:
        n = len(nums)
        nums = [1]+nums+[1]
        dp = [[0 for i in range(n+2)] for j in range(n+2)]

        for i in reversed(range(0, n)):
            for j in range(i+2, n+2):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[j]*nums[k]) 
        return dp[0][-1]
# if __name__ == "__main__":
#     sol = Solution()
#     res = sol.maxCoins([3,1,5,8])
#     print(res)
# @lc code=end

