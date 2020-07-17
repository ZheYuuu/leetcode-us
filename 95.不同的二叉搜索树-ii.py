#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from itertools import product
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        memo = {}
        if n==0:
            return []
        def helper(l,r):
            if l>r:
                return [None]
            if l==r:
                return [TreeNode(l)]
            if (l,r) in memo:
                return memo[(l,r)]
            ans = []
            for i in range(l,r+1):
                a = helper(l,i-1)
                b = helper(i+1, r)
                for pool in product(a,b):
                    root = TreeNode(i)
                    root.left = pool[0]
                    root.right = pool[1]
                    ans.append(root)
            memo[(l,r)] = ans
            return ans
        return helper(1,n)

    def generateTrees(self, n):
        if n==0:
            return []
        def clone(node, offset):
            if not node:
                return None
            new = TreeNode(node.val+offset)
            new.left = clone(node.left, offset)
            new.right = clone(node.right, offset)
            return new
        dp = [[] for _ in range(n+1)]
        dp[0].append(None)
        dp[1].append(TreeNode(1))
        for i in range(2, n+1):
            for j in range(1,i+1):
                for nodeL in dp[j-1]:
                    for nodeR in dp[i-j]:
                        node = TreeNode(j)
                        node.left = nodeL
                        node.right = clone(nodeR, j)
                        dp[i].append(node)
        return dp[-1]

                


            
            
            
# @lc code=end

