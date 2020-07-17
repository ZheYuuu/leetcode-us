#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

# @lc code=start
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        def dfs(s):
            if s in memo:
                return memo[s]
            if not s:
                return []
            res = []
            for word in wordDict:
                if s.startswith(word):
                    if len(word) == len(s):
                        res.append(s)
                        continue
                    a = dfs(s[len(word):])
                    for item in a:
                        res.append(word + " " + item)
            memo[s] = res
            return res
        return dfs(s)

    # def wordBreak(self, s, wordDict):
    #     return self.helper(s, wordDict, {})
    
    # def helper(self, s, wordDict, memo):
    #     if s in memo: return memo[s]
    #     if not s: return []
        
    #     res = []
    #     for word in wordDict:
    #         if not s.startswith(word):
    #             continue
    #         if len(word) == len(s):
    #             res.append(word)
    #         else:
    #             resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
    #             for item in resultOfTheRest:
    #                 item = word + ' ' + item
    #                 res.append(item)
    #     memo[s] = res
    #     return res


if __name__ == "__main__":
    t = Solution().wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"],
#     )
#     print(t)


# @lc code=end

