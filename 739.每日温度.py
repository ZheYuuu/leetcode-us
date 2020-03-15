#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
from collections import deque
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = deque()
        res = [0 for _ in range(len(T))] 
        for i in range(len(T)):
            while(stack and stack[-1][0]<T[i]):
                _, idx = stack.pop()
                res[idx] = i-idx
            stack.append((T[i], i)) 
        while(stack):
            _, idx = stack.pop()
            res[idx] = 0
        return res
    
    def dailyTemperatures(self, T):
        d = deque()
        n = len(T)
        res = [0 for _ in range(n)] 
        for i in range(n):
            while(d and T[d[-1]]<T[i]):
                res[d[-1]] = i-d[-1]
                d.pop()
            d.append(i)
        return res


        
# @lc code=end

