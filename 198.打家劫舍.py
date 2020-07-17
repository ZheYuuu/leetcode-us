#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
    
    def rob(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [0]*(n+1)
        dp[1] = nums[0]
        for i in range(2,n+1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
        return dp[-1]

    
        
# @lc code=end

