#
# @lc app=leetcode.cn id=901 lang=python3
#
# [901] 股票价格跨度
#

# @lc code=start
from collections import deque
class StockSpanner:

    def __init__(self):
        self.d = deque()
        self.idx = 0

    def next(self, price: int) -> int:
        while(self.d and price>=self.d[-1][0]):
            self.d.pop()
        if self.d:
            t = self.idx - self.d[-1][1]
        else:
            t = self.idx - (-1) 
        self.d.append((price, self.idx))
        self.idx += 1
        return t

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

