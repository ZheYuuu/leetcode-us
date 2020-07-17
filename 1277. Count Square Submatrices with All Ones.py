from typing import List
import collections
class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ones = [[0 for _ in range(n+1)] for _ in range(m+1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                ones[i+1][j+1] = ones[i+1][j] + \
                    ones[i][j+1]-ones[i][j] + mat[i][j]
        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(min(m, n)):
                    # if i==2 and j==3 and k==1:
                    #     import ipdb;ipdb.set_trace(context=20)
                    side = k+1
                    r1, c1 = i, j
                    r2, c2 = i-k, j-k

                    if r2 <= 0 or c2 <= 0:
                        continue
                    val = ones[r1][c1] - ones[r1][c2-1] - \
                        ones[r2-1][c1]+ones[r2-1][c2-1]
                    if val == side**2:
                        ans += 1
        return ans


if __name__ == "__main__":
    mat = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]
    Solution().countSquares(mat)
