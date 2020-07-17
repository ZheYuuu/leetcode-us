#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
from typing import List
class Solution:
    # def trap(self, h: List[int]) -> int:
    #     if not h:
    #         return 0
    #     def helper(h, l, r, step):
    #         max_h = h[l]
    #         tmp = 0
    #         res = 0
    #         l+= step
    #         while((l<=r and step>0) or (l>=r and step<0)):
    #             if h[l]>=max_h:
    #                 res += tmp
    #                 max_h = h[l]
    #                 tmp = 0
    #             else:
    #                 tmp += max_h - h[l]
    #             l+= step
    #         return res
    #     maxi = [0] 
    #     n = len(h)
    #     for i in range(n):
    #         if h[i]>h[maxi[0]]:
    #             maxi = [i]
    #         elif h[i] == h[maxi[0]]:
    #             maxi.append(i)
    #     res = 0
    #     pre = 0
    #     for i in maxi:
    #         res += helper(h, pre, i, 1)
    #         pre = i
    #     res += helper(h, n-1, maxi[-1], -1)
    #     return res

    def trap(self, h):
        n = len(h)
        a,b = 0,n-1
        leftmax,rightmax = 0,0
        res = 0
        while(a<b):
            leftmax = max(leftmax, h[a])
            rightmax = max(rightmax, h[b])
            if leftmax<=rightmax:
                res += leftmax - h[a]
                a += 1
            else:
                res += rightmax - h[b]
                b -= 1
            
        return res


# if __name__ == "__main__":
    
#     t = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
#     print(t)
                

            
        
# @lc code=end

