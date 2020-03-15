#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, h) -> int:
        n = len(h)
        l, r = 0, n-1
        res = 0
        while(l<r):
            if h[l]<=h[r]:
                res = max(h[l]*(r-l), res)
                l = l+1
            else:
                res = max(h[r]*(r-l), res)
                r = r-1
        return res

# if __name__ == "__main__":
#     t = Solution().maxArea([1,8,6,2,5,4,8,3,7])
#     print(t)
        
# @lc code=end

