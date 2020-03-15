#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i,num in enumerate(nums):
            if num>=n or num<0:
                nums[i] = 0
        for i in range(n):
            nums[nums[i]%n] += n
        for i in range(1, n):
            if nums[i]//n==0:
                return i
        return n
    
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            # Need loop, because after swap, former A[i] is in right place,
            # but the one swapped at i is not sure.
            while(nums[i]>0 and nums[i]<=n and nums[nums[i]-1]!=nums[i]):
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1

# if __name__ == "__main__":
#     t = Solution().firstMissingPositive([3,4,-1,1])
#     print(t)
        
# @lc code=end

