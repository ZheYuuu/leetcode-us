#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#

# @lc code=start
class Solution:
    mapping = {1:"1", 2:"11", 3:"21", 4:"1211", 5:"111221"}
    def __init__(self):
        self._func()
    def countAndSay(self, n: int) -> str:
        return self.mapping[n]

    def _func(self):
        for i in range(6, 31):
            string = ""
            seq = self.mapping[i-1]
            cnt = 1 
            pre = seq[0]
            for s in seq[1:]: 
                if s==pre:
                    cnt +=1
                else:
                    string += str(cnt)+pre
                    pre = s
                    cnt = 1
            string += str(cnt)+pre
            self.mapping[i] = string




        
# @lc code=end

