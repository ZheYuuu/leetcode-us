#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class UnionFindSet:
    def __init__(self,n):
        self.cnt = n
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, p):
        if p != self.parent[p]:
            p = self.find(self.parent[p])
        return p
    
    def union(self, a, b):
        aRoot = self.find(a)
        bRoot = self.find(b)
        if aRoot==bRoot:
            return
        if self.rank[aRoot]<self.rank[bRoot]:
            self.parent[aRoot] = bRoot
        elif self.rank[aRoot]>self.rank[bRoot]:
            self.parent[bRoot] = aRoot
        else:
            self.parent[aRoot] = bRoot
            self.rank[bRoot] += 1
        self.cnt -= 1 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        ufs = UnionFindSet(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="0":
                    ufs.cnt -=1
                    continue
                if i+1<m and grid[i+1][j]=="1":
                    ufs.union(i*n+j, (i+1)*n+j)
                if j+1<n and grid[i][j+1]=="1":
                    ufs.union(i*n+j, i*n+j+1)
        return ufs.cnt
                    



# @lc code=end

