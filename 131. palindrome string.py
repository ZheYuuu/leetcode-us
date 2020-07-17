from typing import List
class Solution:
    def valid(self, s):
        return s[:]==s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        def helper(s, idx):
            p = []
            for j in range(idx+1,len(s)+1):
                if self.valid(s[idx:j]):
                    if j==len(s):   
                        p.append([s[idx:j]])
                        continue
                    avaliables = helper(s, j)
                    if not avaliables:
                        continue
                    for a in avaliables:
                        t = [s[idx:j]]
                        t.extend(a)
                        p.append(t)
            return p
        return helper(s, 0)
    
    def partition(self, s):
        ans = []
        def dfs(s, i, path):
            if i==len(s):
                ans.append(path[:])
                return
            for j in range(i+1, len(s)+1):
                if self.valid(s[i:j]):
                    path.append(s[i:j])
                    dfs(s, j, path)
                    path.pop()
        dfs(s, 0, [])
        return ans


if __name__ == "__main__":
    sol=Solution()
    print(sol.partition("aabcc"))