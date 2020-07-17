from heapq import *
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i] = dp[i-1]+nums[i-1]
        print(dp)
        ans = 0
        for j in range(1,n+1):
            for i in range(0, j): 
                one_i = dp[i]
                zero_i = i-dp[i]
                one_j = dp[j]
                zero_j = j-dp[j]
                if one_j-one_i==zero_j-zero_i:
                    ans = max(j-i, ans)
                    break
        return ans

if __name__ == "__main__":
    t = Solution().findMaxLength([0,1,0])
    print(t)