#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        ret = []
        intervals.sort() 
        left = intervals[0][0]
        right = intervals[0][1]
        for itv in intervals[1:]:
            if itv[0]<=right:
                right = max(itv[1], right)
            else:
                ret.append([left, right])
                left,right = itv
        ret.append([left, right])
        return ret


# @lc code=end

