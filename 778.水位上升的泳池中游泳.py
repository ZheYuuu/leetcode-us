#
# @lc app=leetcode.cn id=778 lang=python3
#
# [778] 水位上升的泳池中游泳
#

# @lc code=start
import collections


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        _max = 0
        for row in grid:
            _max = max(_max, max(row))

        left = max(0, grid[0][0], grid[-1][-1])
        d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        right = _max + 1
        while left < right:
            mid = left + (right - left) // 2
            if not self.able(grid, mid, d, m, n):
                left = mid + 1
            else:
                right = mid
        return left

    def able(self, grid, k, d, m, n):
        q = collections.deque()
        q.append((0,0))
        vis = [[0 for _ in range(m)] for _ in range(n)]
        while q:
            r, c = q.popleft()
            if r == m - 1 and c == n - 1:
                return True
            for i in range(4):
                rr = r + d[i][0]
                cc = c + d[i][1]
                if (
                    rr >= 0
                    and rr < m
                    and cc >= 0
                    and cc < n
                    and grid[rr][cc] <= k
                    and not vis[rr][cc]
                ):
                    vis[rr][cc] = 1
                    q.append((rr, cc))
        return False
# @lc code=end
