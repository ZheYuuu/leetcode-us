#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        _max = float("-inf")
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or matrix[i][j]=="0":
                    dp[i][j] = int(matrix[i][j])
                    _max = max(_max, dp[i][j])
                    continue
                left = dp[i][j-1]
                up = dp[i-1][j]
                if left==up:
                    dp[i][j] = left+1 if matrix[i-left][j-left]=="1" else left
                else:
                    dp[i][j] = min(left, up)+1
                _max = max(_max, dp[i][j])
        return _max**2
                
                    
                
# @lc code=end

