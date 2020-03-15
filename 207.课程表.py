#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]   # idx指向 val
        for e in prerequisites:
            indegree[e[0]] += 1
            adjacency[e[1]].append(e[0])
        q = []
        for i in range(len(indegree)):
            indegree[i] == 0 and q.append(i)
        while q:
            vertex = q.pop(0)
            numCourses -= 1
            for j in adjacency[vertex]:
                indegree[j] -= 1
                indegree[j] == 0 and q.append(j)
        return numCourses == 0

    def canFinish(self, numCourses, prerequisites):
        if numCourses==0:
            return True
        self.deAdjacency = [set() for _ in range(numCourses)]
        for second, first in prerequisites:
            self.deAdjacency[second].add(first) 
        self.vis = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if self._dfs(i):
                return False
        return True 

    def _dfs(self, vertex):
        if self.vis[vertex]==2:
            return True
        if self.vis[vertex]==1:
            return False
        self.vis[vertex] = 2
        for pre in self.deAdjacency[vertex]:
            if self._dfs(pre):
                return True
        self.vis[vertex] = 1
        return False





if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[0, 1]]))


# @lc code=end

