#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        self.area = 0
        def helper(heights):
            heights = [0]+heights+[0]
            d = deque()
            for i, h in enumerate(heights):
                while(d and h<heights[d[-1]]):
                    width = i-d[-2]-1
                    self.area = max(self.area, heights[d[-1]]*width)
                    d.pop()
                d.append(i)
        m,n  = len(matrix), len(matrix[0])
        h = [0 for _ in range(n)]
        for row in matrix:
            for i in range(n):
                if row[i]=="1":
                    h[i] += 1
                else:
                    h[i] = 0
            helper(h)
        return self.area

# if __name__ == "__main__":
#     t = Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])        
#     print(t)


# @lc code=end

