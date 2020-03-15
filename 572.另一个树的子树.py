#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        return (
            self.isSubtree(s.left, t) or self.isSubtree(s.right, t) or self.helper(s, t)
        )

    def helper(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val:
            return self.helper(s.left, t.left) and self.helper(s.right, t.right)
        return False


# @lc code=end

