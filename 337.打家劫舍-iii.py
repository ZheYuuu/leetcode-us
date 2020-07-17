#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = {None:0}
        def helper(node):
            if not node:
                return 0
            if node in memo:
                return memo[node]
            a = helper(node.left)
            b = helper(node.right)

            aa,bb=0,0
            if node.left:
                aa = helper(node.left.left)+helper(node.left.right)
            if node.right:
                bb = helper(node.right.left) + helper(node.right.right)
            
            t = max(a+b, aa+bb+node.val)
            memo[node] = t
            return t

        helper(root)
        return memo[root]

        
    
       
# @lc code=end

