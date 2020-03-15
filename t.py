from typing import List
import heapq
from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        d = {1: [0, 1], 2: [0, -1], 3: [1, 0], 4: [-1, 0]}
        q = [(0,0,0)]
        m = len(grid)
        n = len(grid[0])
        vis = [[0 for _ in range(n)] for _ in range(m)] 
        while(q):
            cost, i, j = heapq.heappop(q)
            if i==m-1 and j==n-1:
                return cost
            if vis[i][j]:
                continue
            vis[i][j] = 1
            for k,v in d.items():
                r,c = i+d[k][0],j+d[k][1]
                if r<0 or r>=m or c<0 or c>=n or (r,c) or vis[r][c]:
                    continue
                _cost = cost + 1 if grid[i][j]!=k else cost
                heapq.heappush(q, (_cost, r, c))

if __name__ == "__main__":
    t = Solution().minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])
    print(t)

