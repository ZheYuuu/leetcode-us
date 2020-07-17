#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#

# @lc code=start
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        dp  = [1 for _ in range(n)]
        dp_min  = [1 for _ in range(n)]
        ret = float("-inf") 
        for i in range(n):
            dp[i] = max(dp[i-1]*nums[i], dp_min[i-1]*nums[i],nums[i])
            dp_min[i] = min(dp[i-1]*nums[i], dp_min[i-1]*nums[i],nums[i])
            ret = max(ret, dp[i])
        return ret

    def maxProduct(self, nums):
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        maxDp = nums[0] 
        minDp = nums[0]
        ret = nums[0] 
        for i in range(1, n):
            t = maxDp
            maxDp = max(maxDp*nums[i], minDp*nums[i], nums[i])
            minDp = min(t*nums[i], minDp*nums[i], nums[i])
            ret = max(ret, maxDp)
        return ret 

if __name__ == "__main__":
    sol =Solution()
    n = sol.maxProduct([2,-1,1,1])
    print(n)
        
        
# @lc code=end

