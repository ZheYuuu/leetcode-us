#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x+1
        while(left<right):
            mid = left+(right-left)//2
            tmp = mid*mid
            if tmp<x:
                left = mid+1
            elif tmp==x:
                return left
            else:
                right = mid
        return int(left)-1 
# @lc code=end

