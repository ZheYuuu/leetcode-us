#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        rightmost = 0
        ans = 0
        for i in range(n-1):
            rightmost = max(rightmost, i+nums[i])
            if i==end:
                end = rightmost
                ans += 1
        return ans


if __name__ == "__main__":
    t = Solution().jump([1, 2, 1, 1, 1])
    print(t)

# @lc code=end
