#
# @lc app=leetcode.cn id=1000 lang=python3
#
# [1000] 合并石头的最低成本
#

# @lc code=start
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        pre = [0]
        n=len(stones)
        if (n-K)%(K-1)!=0:
            return -1
        for stone in stones:
            pre.append(pre[-1]+stone)
        dp = [[0]*n for n in range(n)]
        
        
        
# @lc code=end

