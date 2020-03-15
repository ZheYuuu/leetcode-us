#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]    # 入度数组:   idx 标识点，val为该点的入度
        adjacency = [set() for _ in range(numCourses)]    # 邻接矩阵   idx 标识点，val为该点指向了哪些点（出）
        ret = []
         # adjacency = [set() for _ in range(numCourses)]  其实用set更好， 可以去重
        for e in prerequisites:   # 这边注意一下e，该题中， e[0]在后，e[1]在先，和普遍的情况有点区别
            indegree[e[0]] += 1
            adjacency[e[1]].add(e[0])
        q = []
        for i in range(len(indegree)):
            indegree[i] == 0 and q.append(i)
        while q:
            vertex = q.pop(0)
            ret.append(vertex)
            for j in adjacency[vertex]:
                indegree[j] -= 1
                indegree[j] == 0 and q.append(j)
        return ret if len(ret)==numCourses else []

if __name__ == "__main__":
    sol = Solution()
    sol.findOrder(2,[[1,0]])
# @lc code=end

