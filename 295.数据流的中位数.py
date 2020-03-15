#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start 
from typing import List
from bisect import bisect_left
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.n = 0
        self.data = []
        

    def addNum(self, num: int) -> None:
        if self.n==0:
            self.data.append(num)
        else:
            pos = self.findPos(num)
            self.data.insert(pos, num)
        self.n+=1
        

        

    def findMedian(self) -> float:
        n = self.n
        if self.n&1==0:
            return (self.data[(n-1)//2]+self.data[(n-1)//2+1])/2
        else:
            return self.data[(n-1)//2]
    
    def findPos(self, num):
        l,r = 0,self.n
        while(l<r):
            mid = (l+r)//2
            if self.data[mid]<num:
                l = mid+1
            else:
                r = mid
        return l

from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [[],[]]

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        n = len(small)+len(large)
        # # even
        # if n&1==0:
        #     if not large or num<=large[0]:
        #         heappush(small,-num)
        #     else:
        #         _num = heappop(large)
        #         heappush(large, num)
        #         heappush(small, -_num)
        # # odd
        # else:
        #     if not small or num>=-small[0]:
        #         heappush(large, num)
        #     else:
        #         _num = heappop(small)
        #         heappush(small, -num)
        #         heappush(large, -_num)
        
        if n&1==0:
            _num = heappushpop(large, num)
            heappush(small, -_num)
        else:
            _num = heappushpop(small, -num)
            heappush(large, -_num)
        
        

    def findMedian(self) -> float:
        small, large = self.heaps
        n = len(small)+len(large)
        if n&1==0:
            return (-small[0]+large[0])/2
        else:
            return -small[0]
        
# if __name__ == "__main__":
#     obj = MedianFinder()
#     obj.addNum(-1)
#     obj.addNum(-2)
#     obj.addNum(-3)
#     print(obj.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

