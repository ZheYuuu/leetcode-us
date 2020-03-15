#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
from typing import List

class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices:
    #         return 0
    #     res = 0
    #     n = len(prices)
    #     i = 0
    #     t = prices[0]
    #     while(i<n-1):
    #         if prices[i+1]>=prices[i]:
    #             i+=1
    #         else:
    #             res += prices[i]-t
    #             t = prices[i+1]
    #             i+=1
    #     if prices[i]>=prices[i-1]:
    #         res += prices[i]-t
    #     return res
    
    def maxProfit(self, prices):
        if not prices:
            return 0
        res = 0
        for i in range(len(prices)-1):
            if prices[i+1]-prices[i]>0:
                res+= prices[i+1]-prices[i]
        return res
            
# if __name__ == "__main__":
#     t = Solution().maxProfit([1,9,6,9,1,7,1,1,5,9,9,9])
#     print(t)
# @lc code=end

