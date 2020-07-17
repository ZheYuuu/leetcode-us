#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        s = set()# 已经确定的顶点
        u = [i for i in range(n)]  # 尚未确定的顶点
        # 初始化邻接矩阵
        adjacency = [
            [float("inf") if i != j else 0 for j in range(n)] for i in range(n)
        ]
        # 初始化起始点到其他点的最短距离
        dist = [float("inf") for i in range(n)]
        dist[src] = 0
        for flight in flights:
            # 更新邻接矩阵
            adjacency[flight[0]][flight[1]] = flight[2]
            # 更新起始点到邻接点的距离
            if flight[0] == src:
                dist[flight[1]] = flight[2]

        def getNearestNode(u, s, dist):
            idx = u[0]
            for i in range(1, len(u)):
                idx = u[i] if dist[idx] > dist[u[i]] else idx
            u.remove(idx)
            s.add(idx)
            return idx

        # 算法主过程
        while u:
            pre = getNearestNode(u, s, dist)
            for i in range(n):
                if i == pre or i in s:
                    continue
                _dist = dist[pre] + adjacency[pre][i]
                if dist[i] > _dist:
                    dist[i] = _dist
        print(dist, sep="\n")


if __name__ == "__main__":
    sol = Solution()
    edges = [
        [0, 1, 1],
        [1, 0, 1],
        [0, 2, 2],
        [2, 0, 2],
        [1, 2, 2],
        [2, 1, 2],
        [1, 4, 3],
        [4, 1, 3],
        [1, 5, 1],
        [5, 1, 1],
        [2, 4, 3],
        [4, 2, 3],
        [3, 4, 5],
        [4, 3, 5],
        [3, 5, 2],
        [5, 3, 2],
        [4, 5, 1],
        [5, 4, 1],
    ]
    sol.findCheapestPrice(6, edges, 0, 2, 1)

# @lc code=end

