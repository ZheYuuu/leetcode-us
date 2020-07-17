from typing import List
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        ones = [[0 for _ in range(n+1)] for _ in range(m+1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                ones[i+1][j+1] = ones[i+1][j] + \
                    ones[i][j+1]-ones[i][j] + mat[i][j]
        lo,hi = 0, min(m,n)
        print(ones)
        for i in range(1, m+1):
            for j in range(1, n+1):
                l = 0
                r = min(min(m,n), j, i)+1
                while(l<r):
                    k = (l+r)//2
                    side = k
                    r1, c1 = i, j
                    r2, c2 = i-k, j-k
                    val = ones[r1][c1] - ones[r1][c2] - \
                        ones[r2][c1]+ones[r2][c2]
                    if val <= threshold:
                        l = k+1
                    else:
                        r = k
                ans = max(l-1, ans)
        return ans

if __name__ == "__main__":
    Solution().maxSideLength([[2,2]],1)