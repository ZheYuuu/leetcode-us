#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
from typing import List
class Solution:



    def search(self, nums: List[int], target: int) -> int:
        def helper(nums, start, end, target):
            if start>end:
                return -1
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>nums[start]:
                if target>=nums[start] and target<=nums[mid]:
                    return bs(nums, start, mid, target)
                else:
                    return helper(nums, mid+1, end, target)
            elif nums[mid]<nums[end]:
                if target>=nums[mid] and target<= nums[end]:
                    return bs(nums, mid, end, target)
                else:
                    return helper(nums, start, mid-1, target)
            return -1
            
        def bs(nums, start, end, target):
            l,r = start, end+1
            while(l<r):
                mid = (l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    l = mid+1
                else:
                    r = mid
            return -1
        
        return helper(nums, 0, len(nums)-1, target)

    def search(self, nums, target):

        l,r = 0, len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[l]:
                if nums[l]<=target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            elif nums[mid]<nums[r]:
                if nums[r]>=target>nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
if __name__ == "__main__":
    t = Solution().search([1,3], 3)
    print(t)
# @lc code=end

