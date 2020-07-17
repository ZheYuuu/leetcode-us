#
# @lc app=leetcode.cn id=857 lang=python3
#
# [857] 雇佣 K 名工人的最低成本
#

# @lc code=start
from typing import List
from heapq import *
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        n = len(quality)
        worker = sorted(zip(quality, wage), key=lambda x: x[1]/x[0])
        heap, ratio, q = [], 0, 0
        for i in range(K):
            heappush(heap, -worker[i][0])
            q += worker[i][0]
            ratio = worker[i][1]/worker[i][0]
        ans = q*ratio
        
        for i in range(K, n):
            heappush(heap, -worker[i][0])
            q+=worker[i][0]
            ratio = worker[i][1]/worker[i][0]

            tmp = -heappop(heap)
            q-=tmp
            ans = min(ans, q*ratio)
        return ans

# if __name__ == "__main__":
#     t = Solution().mincostToHireWorkers([10,20,5],[70,50,30],2)
#     print(t)
        
# @lc code=end

