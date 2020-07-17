#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        queens = []
        # column
        a = {i:False for i in range(n)}
        # diagonal
        b = {i:False for i in range(2*n)}
        # antidiagonal
        c = {i:False for i in range(-n+1,n)}
        self.helper(0, a,b,c, queens, n)
        return self.getSol(n)
    
    def getSol(self,n):
        sol = []
        for queens in self.ans:
            t = [["." for _ in range(n)] for _ in range(n)] 
            for queen in queens:
                t[queen[0]][queen[1]] = "Q"
                t[queen[0]] = "".join(t[queen[0]])
            sol.append(t)
        return sol
        

    
    def helper(self, i, a,b,c, queens,n ):
        if i==n:
            self.ans.append(queens[:])
            return
        for j in range(n):
            if self.valid((i,j), a, b, c):
                a[j] = True
                b[i+j] = True
                c[i-j] = True
                queens.append((i,j))
                self.helper(i+1, a,b,c,queens, n)
                a[j] = False
                b[i+j] = False
                c[i-j] = False
                queens.pop()

        
    def valid(self, pos, a, b, c):
        i = pos[0]
        j = pos[1]
        return not(a[j] or b[i+j] or c[i-j])
# @lc code=end

