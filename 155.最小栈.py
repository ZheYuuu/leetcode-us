#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.helper or self.helper[-1]>=x:
            self.helper.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x==self.helper[-1]:
            self.helper.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helper[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

