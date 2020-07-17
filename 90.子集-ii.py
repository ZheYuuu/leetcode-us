#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = [] 
        def helper(nums, st, path):
            self.ans.append(path[:])
            for i in range(st, len(nums)):
                if i>st and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                helper(nums, i+1, path)
                path.pop()
        helper(nums, 0, [])
        return self.ans

if __name__ == "__main__":
    t = Solution().subsetsWithDup([1,2,2])
    print(t)
# @lc code=end

