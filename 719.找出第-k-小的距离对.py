#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 k 小的距离对
#

# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = nums[-1]-nums[0]
        n = len(nums)
        while(left<right):
            mid = left + (right-left)//2
            cnt = 0
            j = 0
            for i in range(n):
                while (j<n and nums[j]<=nums[i]+mid):
                    j+=1
                cnt += j-i-1
            if cnt<k:
                left = mid+1
            else:
                right = mid
        return left



# @lc code=end

