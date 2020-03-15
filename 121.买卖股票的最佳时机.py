#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1:
            return 0 
        _min = prices[0] 
        ret = 0
        for i in range(1, n):
            if prices[i]>_min:
                ret = max(ret, prices[i]-_min)
            else:
                _min = prices[i]
        return ret

    def maxProfit(self, prices):
        n = len(prices)
        if n<=1:
            return 0
        diff = [prices[i+1]-prices[i] for i in range(n-1)]
        dp = [0 for i in range(n-1)]
        dp[0] = max(diff[0], 0)
        ret = max(dp[0], 0)
        for i in range(1,n-1):
            dp[i] = max(dp[i-1]+diff[i], 0)
            ret = max(dp[i], ret)
        return ret 
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1,2]))

# def dfs(self):
#     stack = [start]
#     vis = []
#     while(stack):
#         node = stack.pop()
#         vis[node] = True
#         neighbors = edges[node]
#         stack.append(left)
#         while(neighbors is not null and not all neighbor visited):
#             node = neighbors[0]
#             vis[node] = True
#             stack.append(left)
#             neighbors = edges[node]
        

# @lc code=end

