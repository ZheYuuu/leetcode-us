#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from typing import List
from collections import deque
class Monoqueue:
    def __init__(self):
        self.mq = deque()
    
    def push(self, n):
        while(self.mq and self.mq[-1]<n):
            self.mq.pop()
        self.mq.append(n)
    
    def pop(self):
        self.mq.popleft()

    @property    
    def front(self):
        return self.mq[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k==0:
            return []
        if k==1:
            return nums
        n = len(nums)
        def clear(d, i, nums, k):
            if d and d[0]==i-k:
                d.popleft()
            while(d and nums[i]>nums[d[-1]]):
                d.pop()
        # Initialize deque
        t = float("-inf")
        d = deque()
        for i in range(k):
            clear(d, i, nums, k)
            d.append(i)
        res = []
        for i in range(k, n):
            res.append(nums[d[0]])
            clear(d, i, nums, k)
            d.append(i)
        res.append(nums[d[0]])
        return res
    
    def maxSlidingWindow(self, nums, k):
        mq = Monoqueue()
        n = len(nums)
        res = []
        for i in range(n):
            if i<k-1:
                mq.push(nums[i])
                continue
            mq.push(nums[i])
            res.append(mq.front)
            if nums[i-k+1]==mq.front:
                mq.pop()
        return res 
            

        
# if __name__ == "__main__":
#     t = Solution().maxSlidingWindow([7,2,4], 2)
#     print(t)




            

# @lc code=end

