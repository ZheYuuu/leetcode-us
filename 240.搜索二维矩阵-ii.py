#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def helper(a, l, r, target):
            while(l<r):
                mid = (l+r)//2
                if a[mid]<target:
                    l = mid+1
                else:
                    r = mid
            return l
        m = len(matrix)
        if m==0:
            return False
        n = len(matrix[0])
        if n==0:
            return False
        a = [row[0] for row in matrix]
        k = helper(a, 0, m, target)
        if k<m and matrix[k][0]==target:
            return True
        for i in range(k):
            row = matrix[i]
            if row[-1]<target:
                continue
            t = helper(row, 0, n, target)
            if row[t]==target:
                return True
        return False
    
    def searchMatrix(self, matrix, target ):
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i,j = m-1, 0 
        while(i>=0 and j<n):
            if matrix[i][j]<target:
                j = j+1
            elif matrix[i][j]>target:
                i = i-1
            else:
                return True
        return False

# if __name__ == "__main__": sol = Solution() data = [ ([[-5]],-5), ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20) ]
#     for d in data:
#         t = sol.searchMatrix(*d)
#         print(t)

        
# @lc code=end

