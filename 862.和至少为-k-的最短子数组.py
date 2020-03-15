#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#

# @lc code=start
from typing import List
from collections import deque
class Solution:
    
    def shortestSubarray(self, A,K):
        B = [0]
        for a in A:
            B.append(B[-1]+a)
        # Monotonic Incresing deque
        d = deque()
        res = float("inf")
        for i, b in enumerate(B):
            # why pop? Maintain property of monotonic. 
            # Why monotonic is useful? 

            while(d and B[d[-1]]>b):
                d.pop()
            # which while first no matter.
            while(d and B[d[0]]<=b-K):
                res = min(res, i-d[0])
                d.popleft()
            d.append(i)
        return res if res<float("inf") else -1 

    # Follow up: What about longest subarray with sum at most K?
    # Oh no... A=[3,2,-1,-2,3,4], K=1
    def shortestSubarray(self, A, K):
        B = [0]
        for a in A:
            B.append(B[-1]+a)
        # Monotonic Incresing deque
        d = deque()
        res = float("inf")
        for i,b in enumerate(B):
            while(d and b<B[d[-1]]):
                d.pop()
            while(d and B[d[0]]>=b-K):
                res = max(res, i-d[0])
                d.popleft()
            d.append(i)

#  if __name__ == "__main__":
#     t = Solution().shortestSubarray([2,-1,2], 4)
#     print(t)


        
# @lc code=end


