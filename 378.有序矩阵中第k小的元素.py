#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#

# @lc code=start


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        first = matrix[0][0]
        last = matrix[-1][-1]
        while first < last:
            mid = first + (last - first) // 2
            cnt = self.smallerCount(matrix, mid)
            if cnt < k:
                first = mid + 1
            else:
                last = mid
            print(mid, cnt, first, last)
        print(f"first, {first}, last:{last}")
        return first

    def smallerCount(self, matrix, num):
        m = len(matrix)
        n = len(matrix[0])
        cnt = 0
        for i in range(m):
            left = 0
            right = n
            while left < right:
                mid = left + (right - left) // 2
                if matrix[i][mid] <= num:
                    left = mid + 1
                else:
                    right = mid
            cnt += left
        return cnt


# @lc code=end
