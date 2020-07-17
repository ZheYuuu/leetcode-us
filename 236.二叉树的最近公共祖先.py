#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     def lowestCommonAncestor(
#         self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
#     ) -> "TreeNode":
#         def helper(node, target, path):
#             if not node or self.flag:
#                 return 
#             if node == target:
#                 self.path = path[:]
#                 self.flag=True
#                 return  True
#             left = node.left
#             path.append(left)
#             helper(left, target, path)
#             path.pop()

#             right = node.right
#             path.append(right)
#             helper(right, target, path)
#             path.pop()

#         self.flag=False
#         self.path = []
#         path_a = [root]
#         helper(root, p, path_a)
#         path_a = self.path[:]

#         self.flag=False
#         self.path = []
#         path_b = [root]
#         helper(root, q, path_b)
#         path_b = self.path[:] 
#         for i in path_a[::-1]:
#             for j in path_b:
#                 if i==j:
#                     return i
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if p==root or q==root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if not left:
            return right
        else:
            return left



# @lc code=end

