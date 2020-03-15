#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        candidate = None
        for num in nums:
            if cnt==0:
                candidate= num
            if num==candidate:
                cnt+=1
            else:
                cnt -= 1
        return candidate
if __name__ == "__main__":
    sol = Solution()        
    sol.majorityElement([3,2,3])
# @lc code=end
