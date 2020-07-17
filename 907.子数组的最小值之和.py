#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    # Brute Force, TLE
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                ans += min(A[i : j + 1])
                ans = ans % (7 + 10 ** 9)
        return ans

    # Stack
    # 想用239的思路，用大小为k的窗口去找。需要用n个窗口去找，复杂度为O(n^2)，TLE
    def sumSubarrayMins(self, A):
        n = len(A)
        ans = 0
        for i in range(1, n + 1):
            d = deque()
            local = 0
            for j, a in enumerate(A):
                while d and j - d[0] == i:
                    d.popleft()
                while d and a < A[d[-1]]:
                    d.pop()
                d.append(j)
                if j >= i - 1:
                    local += A[d[0]]
            ans = (ans + local) % (10 ** 9 + 7)
        return ans

    #
    def sumSubarrayMins(self, A):
        n = len(A)
        ans = 0
        mod = 10 ** 9 + 7
        d = deque()
        PLE = [0 for _ in range(n)]
        NLE = [n-i for i in range(n)]
        # Find previous less element
        for i, a in enumerate(A):
            while d and A[d[-1]] > a:
                d.pop()
            if not d:
                # 注意，如果PLE为空，说明当前值比从起点开始到当前的所有的元素都要小
                PLE[i] = i-(-1)
            else:
                PLE[i] = i-d[-1] 
            d.append(i)
        # Find next less element
        d = deque()
        for i, a in enumerate(A):
            while d and A[d[-1]] > a:
                NLE[d[-1]] = i - d[-1]
                d.pop()
            d.append(i)
        for i in range(n):
            ans = (ans + A[i] * PLE[i] * NLE[i]) % mod
        return ans



# if __name__ == "__main__":
#     t = Solution().sumSubarrayMins([3, 1, 2, 4])
#     print(t)


# @lc code=end

