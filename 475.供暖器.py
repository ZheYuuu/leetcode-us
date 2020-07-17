#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#

# @lc code=start


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters.insert(0, float("-inf"))
        heaters.append(float("inf"))
        ret = 0
        for house in houses:
            left = 0
            right = len(heaters)
            while(left < right):
                mid = left + (right-left)//2
                if heaters[mid] < house:
                    left = mid+1
                else:
                    right = mid
            heater = heaters[left]
            if house >= heater:
                ret = max(ret, house-heater)
            else:
                ret = max(ret, min(heater-house, house-heaters[left-1]))
        return ret


# @lc code=end
