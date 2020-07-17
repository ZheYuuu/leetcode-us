#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
import math
class Solution:
    def numSquares(self, n: int) -> int:
        m = int(math.sqrt(n))
        nums = [i*i for i in range(1, m+1)]
        dp = [float("inf") for i in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            for num in nums:
                if i>=num:
                    dp[i] = min(dp[i], dp[i-num]+1)
        return dp[-1]


    def numSquares(self, n):
        nums = []
        vis = [0 for i in range(n+1)]
        # 注意用set，不然会多出很多重复的待搜索节点
        q = set([(0,0)])
        vis[0] = 1
        for i in range(1, int(n**0.5)+1):
            nums.append(i*i)
        while(q):
            _q = set()
            for curr, depth in q:
                for num in nums:
                    if curr+num == n:
                        return depth +1
                    elif curr+num <n:
                        _q.add((curr+num, depth+1))
                    else:
                        break
            q = _q
        
# 静态dp
class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]


# if __name__ == "__main__":
#     t = Solution().numSquares(7168)
#     print(t)
        
# @lc code=end

