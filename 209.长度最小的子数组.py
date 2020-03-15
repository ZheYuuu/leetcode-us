#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        l, r=0,0
        t = 0 
        res = n+1
        while(l<=r and r<=n):
            if t>=s:
                res = min(r-l, res)
                if l==r:
                    return 1
                t = t-nums[l]
                l = l+1
            else:
                if r<n:
                    t = t+nums[r]
                r = r+1
        return res if res!=n+1 else 0

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        l, r=0,0
        t = 0 
        res = n+1
        while(r<n):
            t+= nums[r]
            while(t>=s):
                res = min(r-l+1, res)
                t -= nums[l]
                l = l+1
            r = r+1
        return res if res!=n+1 else 0

# if __name__ == "__main__":
#     t = Solution().minSubArrayLen(7,[2,3,1,2,4,3])
#     print(t)
            


# @lc code=end

