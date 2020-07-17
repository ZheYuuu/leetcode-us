#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
import bisect
# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                return True 
            if nums[mid]==nums[l]==nums[r]:
                l += 1
                r -= 1
                continue
            # 左半部分有序
            if nums[l]<=nums[mid]:
                # target在左部分
                if nums[l]<=target<nums[mid]:
                    r = mid-1
                # target在右部分
                else:
                    l = mid+1
            # 右半部分有序
            else:
                if nums[r]>=target>nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
        return False

# if __name__ == "__main__":
#     t = Solution().search([3,4,5,6,0,1,2],1)
#     print(t)
# @lc code=end

