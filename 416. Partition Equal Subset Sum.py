from copy import deepcopy
from typing import List
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        dislikes.sort()
        g = {}
        idx = 0
        print(dislikes)
        def dfs(dislikes, idx, g):
            if idx==len(dislikes):
                print("!!!")
                return True
            for i in range(idx, len(dislikes)):
                a = dislikes[i][0]
                b = dislikes[i][1]
                if a not in g:
                    g[a] = 0
                    g[b] = 1
                    case1 = dfs(dislikes, i+1, deepcopy(g))
                    g[a] = 1
                    g[b] = 0
                    case2 = dfs(dislikes, i+1, deepcopy(g))
                    return case1 or case2
                else:
                    if b not in g:
                        g[b] = g[a]^1
                    else:
                        if g[b]==g[a]:
                            print(g)
                            print("error: ", a, b)
                            return False
            return True
        dfs(dislikes, 0, g)
                
if __name__ == "__main__":
    Solution().possibleBipartition(22, [[1,4],[2,22],[4,22]])