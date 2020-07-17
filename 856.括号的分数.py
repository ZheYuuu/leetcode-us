#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] 括号的分数
#

# @lc code=start
class Solution:
    # divede-conquer 
    def scoreOfParentheses(self, S: str) -> int:
        def helper(s, i, j):
            ans = 0
            bal = 0
            for k in range(i,j):
                if s[k]=="(":
                    bal += 1
                else:
                    bal -= 1 
                if bal==0:
                    # ()，相当于base case
                    if k-i==1:
                        ans +=1
                    else:
                        ans += 2*helper(s, i+1,k)
                    i = k+1
            return ans
        return helper(S, 0, len(S))
    
    # stack
    def scoreOfParentheses(self, S):
        curr = 0
        stack = []
        for s in S:
            if s=="(":
                stack.append(curr)
                curr = 0
            else:
                curr += stack.pop() + max(curr, 1)
        return curr
    
    # stack
    def scoreOfParentheses(self, S):
        # keep total score
        stack = [0]
        for s in S:
            if s=="(":
                stack.append(0)
            else:
                t = stack.pop()
                # zero means single parentheses
                if t==0:
                    stack[-1]+= 1
                # not zero means inner parentheses exists.
                else:
                    stack[-1] += 2*t
        return stack[0] 

        
# @lc code=end

