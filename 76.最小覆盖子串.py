#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        target = collections.defaultdict(int)
        for w in t:
            target[w] += 1
        left, right = 0, 0  
        self.ret, self._global = "", float("inf")
        match = 0 
        cntMap = collections.defaultdict(int)
        while left < n and right < n:
            while right < n and match<len(target):
                if s[right] in target:
                    cntMap[s[right]] += 1
                    if cntMap[s[right]]==target[s[right]]:
                        match+=1
                right += 1
            
            # unable to find all
            if match != len(target):
                return self.ret 
            self.judge(s, left, right)
            # remove elements to make lookup<target
            # 此处循环不变量为 s[left,right) 包含T的所有字母
            while left < n:
                tmp = s[left]
                if tmp in target:
                    cntMap[tmp] -= 1
                    if cntMap[tmp]<target[tmp]:
                        match -= 1
                    if match < len(target):
                        left += 1
                        break
                # 于此处进行紧缩
                left += 1
                self.judge(s, left, right)
            # print(left, right, s[left:right])
        return self.ret

    def judge(self,s, left, right):
        if self._global > right - left:
            self._global = right - left
            self.ret = s[left:right]
    
    # def contains(self, target, source):
    #     for key,val in target.items():
    #         if key not in source or val>source[key]:
    #             return False
    #     return True


if __name__ == "__main__":
    sol = Solution()
    s = sol.minWindow("aa", "aa")
    # s = sol.minWindow("ADOBECODEBANC", "ABC")
    print(s)
# @lc code=end

