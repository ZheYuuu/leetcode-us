#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if k>n//2:
            t = prices[0]
            ans = 0
            for i in range(1, n):
                if prices[i]>=t:
                    ans += prices[i]-t
                t = prices[i]
            return ans
        hold = [[0]*(n+1) for _ in range(k+1)]
        unhold = [[0]*(n+1) for _ in range(k+1)]
        # This base case should be concerned.
        for i in range(1,k+1):
            hold[i][0] = -prices[0]
        for i in range(1, k+1):
            for j in range(1, n+1):
                hold[i][j] = max(unhold[i-1][j-1]-prices[j-1], hold[i][j-1])
                unhold[i][j] = max(hold[i][j-1]+prices[j-1], unhold[i][j-1])
        return unhold[-1][-1]
# @lc code=end

