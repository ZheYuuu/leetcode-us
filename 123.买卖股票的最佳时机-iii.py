#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        k = 2
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

