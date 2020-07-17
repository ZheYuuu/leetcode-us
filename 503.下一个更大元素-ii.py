#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = deque()
        res = [-1 for _ in range(n)]
        nums = nums+nums
        for i,num in enumerate(nums):
            while(d and num>nums[d[-1]]):
                res[d[-1]%n] = num
                d.pop()
            d.append(i)
        return res



                
        
# @lc code=end

