#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        n = len(s)
        tmp = {}
        local, ret = 0, 0
        # 第一个while中维护一个循环不变量：$[left, right)$间元素都已经被计入，且无重复元素。
        # 也就是说s[left]到s[right-1]间都被加入了tmp， 而tmp[s[right]]一定为False.
        # 
        while left <= right and left < n and right < n:
            # right一直向后探索，直到触底或者遇到重复元素
            while right < n and (s[right] not in tmp or tmp[s[right]] == False):
                tmp[s[right]] = True
                right += 1
            ret = max(ret, right - left)
            # 触底
            if right == n:
                continue
            # 遇到重复元素，为了维护循环变量的性质，那就要删去原来的，加入新的
            # while 寻找旧的重复元素位置，同时移出tmp
            while left < n and s[left] != s[right]:
                tmp[s[left]] = False
                left += 1
            # 此时s[left],s[right]指向的元素相等，就是重复元素
            # 下面两步很重要
            tmp[s[right]] = False   #维护[left, right)，所以right此时不能加入tmp
            left += 1   # left要指向旧的重复元素的后一位
        return ret


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("tmmzuxt"))