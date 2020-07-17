#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root)[2] 

    def helper(self, node):
        _max = node.val
        _min = node.val
        if node.left:
            left_min, left_max, flag = self.helper(node.left)
            if node.val <= left_max or not flag:
                return 0, 0, False
            _min = min(_min, left_min)
            _max = max(_max, left_max)
        if node.right:
            right_min, right_max, flag = self.helper(node.right)
            if node.val >= right_min or not flag:
                return 0, 0, False
            _min = min(_min, right_min)
            _max = max(_max, right_max)
        return _min, _max, True


# @lc code=end
