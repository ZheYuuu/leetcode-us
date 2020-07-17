#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n-2):
            l,r = i+1,n-1
            if nums[i]>0:
                break
            # If the number is the same as the number before, we have used it as target already, continue. 
            # This strategy save a lot of time.
            if i>0 and nums[i]==nums[i-1]:
                continue
            while(l<r):
                t = nums[l]+nums[r]
                if t>-nums[i]:
                    r = r-1
                elif t<-nums[i]:
                    l = l+1
                else:
                    res.add((nums[i],nums[l],nums[r]))
                    l = l+1
        res = [list(i) for i in res]
        return res

# @lc code=end

