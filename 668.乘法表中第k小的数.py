#
# @lc app=leetcode.cn id=668 lang=python3
#
# [668] 乘法表中第k小的数
#

# @lc code=start


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        first = 1
        last = m*n
        while(first < last):
            mid = first + (last-first)//2
            cnt = self.helper(m, n, mid, k)
            if self.helper(m, n, mid, k) < k:
                first = mid+1
            else:
                last = mid
        return first

    def helper(self, m, n, target, k):
        cnt = 0
        for row in range(1, m+1):
            cnt += min(n, target//row)
        if cnt > k:
            return cnt
        return cnt


# @lc code=end
