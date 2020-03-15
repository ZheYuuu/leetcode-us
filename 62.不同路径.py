#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==n==0:
            return 0
        pre = [1 for i in range(n)]
        for i in range(1, m):
            curr = [1 for i in range(n)]
            for j in range(1, n):
                curr[j] = curr[j-1]+pre[j]
            pre = curr
        return pre[-1]
        
# @lc code=end

