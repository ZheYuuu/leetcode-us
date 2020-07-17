#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        t = sorted(nums)
        l = 0
        r = len(t)-1
        while(l<len(t)):
            if t[l] != nums[l]:
                break
            l+=1
        while(r>=0):
            if t[r] != nums[r]:
                break
            r -= 1
        return r-l+1 if r>l else 0

# @lc code=end

