#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:

    def totalNQueens(self, n: int) :
        self.ans = 0
        # column
        a = {i:False for i in range(n)}
        # diagonal
        b = {i:False for i in range(2*n)}
        # antidiagonal
        c = {i:False for i in range(-n+1,n)}
        self.helper(0, a,b,c , n)
        return self.ans
    
        

    
    def helper(self, i, a,b,c,n ):
        if i==n:
            self.ans += 1
            return
        for j in range(n):
            if self.valid((i,j), a, b, c):
                a[j] = True
                b[i+j] = True
                c[i-j] = True
                self.helper(i+1, a,b,c, n)
                a[j] = False
                b[i+j] = False
                c[i-j] = False

        
    def valid(self, pos, a, b, c):
        i = pos[0]
        j = pos[1]
        return not(a[j] or b[i+j] or c[i-j])
# @lc code=end

