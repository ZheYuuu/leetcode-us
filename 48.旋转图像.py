#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 方法1： 四个角旋转
        # for i in range(n // 2):
        #     # for j in range((n+1)//2) 两者一样
        #     for j in range(i, n - i - 1):
        #         tmp = matrix[i][j]
        #         matrix[i][j] = matrix[n - j - 1][i]
        #         matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
        #         matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
        #         matrix[j][n - i - 1] = tmp

        # 方法2： clockwise rotate: reverse up to down, then swap the symmetry
        #        anticlockwise rotate: swap the symmetry(主对角线), then reverse up to down  
        #   解释：https://en.wikipedia.org/wiki/Examples_of_groups#dihedral_group_of_order_8
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        


# @lc code=end

