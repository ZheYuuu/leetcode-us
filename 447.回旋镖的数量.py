#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#

# @lc code=start
from typing import List
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dis(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        n = len(points)
        ret = 0
        for i in range(n):
            hashmap = {}
            for j in range(0, n):
                if i==j:
                    continue
                d = dis(points[i], points[j])
                hashmap[d] = hashmap.get(d, 0) + 1
                if hashmap[d]>1:
                    ret += (hashmap[d]-1)*2
        return ret

# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    k = sol.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])
    print(k)