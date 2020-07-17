from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # n = len(nums)
        # dp = [[None for _ in range(S+1)] for _ in range(n+1)]
        # dp[0][0] = 0
        # for i in range(1, n+1):
        #     for j in range(1, S+1):
        #         a,b = 0,0
        #         if j-nums[i-1]
        #         dp[i][j] = 
        n = len(nums)
        diff = S+sum(nums)
        if diff & 1 ==1 or sum(nums)<S:
            return 0
        target = diff//2
        dp = [[None for _ in range(target+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        print("target:", target)
        for i in range(1, n+1):
            for j in range(0, target+1):
                if j-nums[i-1]>=0 and dp[i-1][j-nums[i-1]]  is not None:
                    a = dp[i-1][j-nums[i-1]]
                else:
                    a = 0
                if dp[i-1][j] is not None:
                    b = dp[i-1][j]
                else:
                    b = 0
                    
                dp[i][j] = a+b
        print(dp)
        if dp[-1][-1] is None:
            return 0
        return dp[-1][-1]
                
if __name__ == "__main__":
    print(Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1],1))
