#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        vis = [0 for _ in nums]
        m = len(nums)
        if m==1:
            return True

        def dfs(pos, nums):
            flag = False
            for i in reversed(range(nums[pos])):
                j = pos+i+1
                if j>=m-1:
                    return True
                if j<m and not vis[j]:
                    vis[j] = 1
                    flag = flag or dfs(j, nums)
                    if flag:
                        return flag
            return flag
        return dfs(0, nums)

    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        if len(nums)==1:
            return True
        while(True):
            t = idx 
            for i in range(nums[idx]):
                pos = idx +i+1
                if pos>=len(nums)-1 or pos+nums[pos]>=len(nums)-1:
                    return True
                t = max(pos+nums[pos], t)
            if t==idx:
                return False
            idx = t 
    
    def canJump(self, nums):
        dp = [-1 for _ in nums]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            for j in range(0,i):
                if dp[j]-i>=0:
                    dp[i] = max(nums[j], dp[i])
        return dp[-1]>=0
    
    def canJump(self, nums):
        max_i = 0
        for i,val in enumerate(nums):
            if max_i<i:
                return False
            if i+val>max_i:
                max_i = i+val
        return max_i>=len(nums)-1





    
if __name__ == "__main__":
    sol = Solution()
    arr = [3,2,1,0,4]
    print(sol.canJump(arr))
        
# @lc code=end

