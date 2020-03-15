#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums, i, path):
            res.append(path[:]) 
            if i==len(nums):
                return
            for j in range(i, len(nums)):
                path.append(nums[j])
                helper(nums, j+1, path)
                path.pop()
        helper(nums, 0, [])
        return res
# if __name__ == "__main__":
#     t = Solution().subsets([])
#     print(t)
# @lc code=end

