#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights  = [0]+heights + [0]
        res = 0
        for i in range(len(heights)):
            while(stack and heights[i]<heights[stack[-1]]):
                width = i-stack[-2]-1
                res = max(width*heights[stack[-1]], res)
                stack.pop()
            stack.append(i)
        return res
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        heights = [0]+heights+[0]
        # monotic incresing queue
        q = [0]
        n = len(heights)
        ans = 0 
        for i in range(1, n):
            while(q and heights[i]<heights[q[-1]]):
                curr = q.pop()
                left = q[-1]
                right = i
                ans = max(heights[curr]*(right-left-1), ans)
            q.append(i)
        return ans 
    

# if __name__ == "__main__":
#     t = Solution().largestRectangleArea([2,1,2])
#     print(t)
    


# @lc code=end

