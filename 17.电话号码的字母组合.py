#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        l = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []
        def dfs(digits, path):
            if not digits:
                res.append(path)
                return 
            for ch in l[digits[0]]:
                dfs(digits[1:], path+ch)
        dfs(digits, '')
        return res

# if __name__ == "__main__":
#     t = Solution().letterCombinations("23")
#     print(t)



# @lc code=end

