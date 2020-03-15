#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def func(nums):
            if not nums:
                return 0
            n = len(nums)
            dp = [0]*(n+1)
            dp[1] = nums[0]
            for i in range(2, n+1):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
            return dp[-1]
        n = len(nums)
        if n==1:
            return nums[0]
        a = func(nums[:n-1])
        b = func(nums[1:])
        return max(a,b)
# @lc code=end

