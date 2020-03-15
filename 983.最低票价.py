#
# @lc app=leetcode.cn id=983 lang=python3
#
# [983] 最低票价
#

# @lc code=start
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        times = {0: 1, 1: 7, 2: 30}
        res = {}

        def dfs(idx, curr, cost):
            if idx in res:
                return res[idx]
            if idx >= n:
                return cost
            if curr >= days[idx]:
                return dfs(idx + 1, curr, cost)
            tmp = float("inf")
            for i, val in enumerate(costs):
                tmp = min(tmp, dfs(idx + 1, days[idx]+ times[i]-1, cost + val))
            res[idx] = tmp
            return tmp
        t = float("inf")
        for i in range(2):
            t = min(dfs(1,days[0]+times[i]-1,costs[i]), t)
        return t

if __name__ == "__main__":
    sol = Solution()
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    print(sol.mincostTickets(days, costs))
    t = sol.mincostTickets([1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28], [3, 13, 45])
    print(t)

# @lc code=end

