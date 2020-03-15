#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n+1)]        
        res = nums[0] 
        for i in range(1, n+1):
            dp[i] = max(nums[i-1], dp[i-1]+nums[i-1])
            res = max(res, dp[i])
        return res

    def maxSubArray(self, nums):
        n = len(nums)
        def span(nums, l, r, mid):
            left_max,right_max = float("-inf"),float("-inf") 
            i = mid
            t = 0
            while(i>=l):
                t = t+nums[i]
                left_max = max(left_max, t)
                i-=1
            j = mid+1
            t = 0
            while(j<=r):
                t = t+nums[j]
                right_max = max(right_max, t)
                j += 1
            return right_max+left_max

            
        def helper(nums, l, r):
            if l>r:
                return float("-inf")
            if l==r:
                return nums[l] 
            mid = (l+r)//2
            max1 = helper(nums, l, mid)
            max2 = helper(nums, mid+1, r)
            max3 = span(nums, l, r, mid)
            return max(max1,max2,max3)
        return helper(nums, 0, n-1)

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n+1)]        
        res = nums[0] 
        end = 0
        for i in range(1, n+1):
            dp[i] = max(nums[i-1], dp[i-1]+nums[i-1])
            if res<dp[i]:
                res = dp[i]
                end = i
        start, end = self.getPath(nums, dp, end)
        print(nums[start: end+1])
        return res 

    def getPath(self, nums, dp, end):
        t = dp[end]
        i=end-1
        while(i>=0 and t!=0):
            t -= nums[i]
            i -= 1
        return i+1, end-1





if __name__ == "__main__":
    t = Solution().maxSubArray([3,4,-1,1])
    t = Solution().maxSubArray( [-2,1,-3,4,-1,2,1,-5,4])
    print(t)
# @lc code=end

