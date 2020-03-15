#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        loopup = {}
        for a in nums2:
            while stack and a>stack[-1]:
                loopup[stack[-1]] = a
                stack.pop()
            stack.append(a)
        res = []
        for b in nums1:
            if b in loopup:
                res.append(loopup[b])
            else:
                res.append(-1)
        return res

# @lc code=end

