#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132模式
#

# @lc code=start
from collections import deque
from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        d = deque()
        a2 = None
        for i in reversed(range(len(nums))):
            # 只要a2有值，就说明d里存在a3,那就只要找到a1就可以了。
            # 又由于a2是维护的最大值，所以直接和a2比较即可
            if a2 and a2>nums[i]:
                return True
            while(d and nums[d[-1]]<nums[i]):
                if a2:
                    a2 = max(a2, nums[d[-1]])
                else:
                    a2 = nums[d[-1]]
                d.pop()
            d.append(i)
        return False

# if __name__ == "__main__":
#     t = Solution().find132pattern([3,1,4,2])
#     print(t)

        
# @lc code=end

