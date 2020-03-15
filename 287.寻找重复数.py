#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        while(True):
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast==slow:  break
        fast = 0
        while(fast!=slow):
            fast = nums[fast]
            slow = nums[slow]
        return fast
        

        
# @lc code=end

