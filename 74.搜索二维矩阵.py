#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = []
        [m.extend(row) for row in matrix]
        left = 0
        right = len(m) 
        while(left<right):
            mid = left + (right-left)//2
            if m[mid]==target: 
                return True
            elif m[mid]<target:
                left = mid+1
            else:
                right = mid
        return False
# @lc code=end
