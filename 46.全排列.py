#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List
class Solution:
    def hash(self, nums):
        return "".join(map(str, nums))

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.memo = {}
        return self.helper(nums)
    
    def helper(self, nums):
        if len(nums)==0:
            return [[]] 
        h = self.hash(nums)
        if h in self.memo:
            return self.memo[h]
        ans = []
        for i in range(len(nums)):
            num = nums[i]
            seqs = self.helper(nums[:i]+nums[i+1:])
            for seq in seqs:
                t = [num]
                t.extend(seq)
                ans.append(t)
        self.memo[h] = ans
        return ans 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(nums, ava, path):
            if not ava:
                self.ans.append(path[:])
                return
            for a in ava:
                ava.remove(a)
                path.append(a)
                dfs(nums, ava, path)
                ava.add(a)
                path.pop()
        dfs(nums, set(nums), [])
        return self.ans

if __name__ == "__main__":
    sol = Solution()
    t = sol.permute([1,2,3])
    print(t)




# @lc code=end

