#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def helper(i, nums):
            if nums[i]!=0:
                return
            j = i
            while(j<n):
                if nums[j]!=0:
                    nums[i], nums[j] = nums[j], nums[i]
                    return 
                j = j+1

        for i in range(n):
            helper(i, nums)
        return nums
    
    def moveZeroes(self, nums):
        slow = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[slow] = nums[slow],nums[i]
                slow += 1
        return nums


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.moveZeroes([0,0,0,0,0]))

        
# @lc code=end

