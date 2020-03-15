#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
class Solution:
    # 解法1： 第一次二分nums1和nums2的取值范围，得到mid，
    # 用这个mid到nums1和nums2中去判断是不是中位数， 判断过程为第二次二分
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     m = len(nums1)
    #     n = len(nums2)
    #     if (m + n) % 2 == 0:
    #         t = (m + n) // 2
    #         return (self.helper(nums1, nums2, t) + self.helper(nums1, nums2, t + 1)) / 2
    #     else:
    #         t = (m + n) // 2
    #         return self.helper(nums1, nums2, t + 1)

    # def helper(self, a, b, target):
    #     left,right = 0, 0
    #     if a:
    #         left = min(left, a[0])
    #         right = max(right, a[-1])
    #     if b:
    #         left = min(left, b[0])
    #         right = max(right, b[-1])
    #     while left < right:
    #         mid = left + (right - left) // 2
    #         cnt = self.smallerCnt(a, mid) + self.smallerCnt(b, mid)
    #         if cnt < target:
    #             left = mid + 1
    #         else:
    #             right = mid
    #     return left

    # def smallerCnt(self, arr, target):
    #     left = 0
    #     right = len(arr)
    #     while left < right:
    #         mid = left + (right - left) // 2
    #         if arr[mid] <= target:
    #             left = mid + 1
    #         else:
    #             right = mid
    #     return left

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        k = (len(nums1) + len(nums2) + 1) >> 1
        while left < right:
            m1 = left + (right-left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1
        nums1LeftMax = float("-inf") if m1 == 0 else nums1[m1 - 1]
        nums1RightMin = float("inf") if m1 == len(nums1) else nums1[m1]

        nums2LeftMax = float("-inf") if m2 == 0 else nums2[m2 - 1]
        nums2RightMin = float("inf") if m2 == len(nums2) else nums2[m2]

        if (len(nums1) + len(nums2)) & 1:
            return max(nums1LeftMax, nums2LeftMax)
        else:
            return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin))/2

    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     # 为了让搜索范围更小，我们始终让 num1 是那个更短的数组，PPT 第 9 张
    #     if len(nums1) > len(nums2):
    #         # 这里使用了 pythonic 的写法，即只有在 Python，中可以这样写
    #         # 在一般的编程语言中，得使用一个额外变量，通过"循环赋值"的方式完成两个变量的地址的交换
    #         nums1, nums2 = nums2, nums1

    #     # 上述交换保证了 m <= n，在更短的区间 [0, m] 中搜索，会更快一些
    #     m = len(nums1)
    #     n = len(nums2)

    #     # 使用二分查找算法在数组 nums1 中搜索一个索引 i，PPT 第 9 张
    #     left = 0
    #     right = m

    #     # 因为 left_total 这个变量会一直用到，因此单独赋值，表示左边粉红色部分一共需要的元素个数
    #     left_total = (m + n + 1) >> 1
    #     while left < right:
    #         # 尝试要找的索引，在区间里完成二分，为了保证语义，这里就不定义成 mid 了
    #         # 用加号和右移是安全的做法，即使在溢出的时候都能保证结果正确，但是 Python 中不存在溢出
    #         # 参考：https://leetcode-cn.com/problems/guess-number-higher-or-lower/solution/shi-fen-hao-yong-de-er-fen-cha-zhao-fa-mo-ban-pyth/
    #         i = (left + right) >> 1
    #         j = left_total - i
    #         print(i,j)

    #         # 如果 nums1 左边最大值 > nums2 右边最小值
    #         if nums2[j - 1] > nums1[i]:
    #             # 这个分支缩短边界的原因在 PPT 第 8 张，情况 ①
    #             left = i + 1
    #         else:
    #             # 这个分支缩短边界的原因在 PPT 第 8 张，情况 ②
    #             # 【注意】：不让它收缩的原因是讨论 nums1[i - 1] > nums2[j]，i - 1 在数组的索引位置，在 i = 0 时越界
    #             right = i
    #     print(f"m1:{i}")
    #     # 退出循环的时候，交叉小于等于一定关系成立，那么中位数就可以从"边界线"两边的数得到，原因在 PPT 第 2 张、第 3 张
    #     i = left
    #     j = left_total - left

    #     # 边界值的特殊取法的原因在 PPT 第 10 张
    #     nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
    #     nums1_right_min = float('inf') if i == m else nums1[i]

    #     nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
    #     nums2_right_min = float('inf') if j == n else nums2[j]

    #     # 已经找到解了，分数组之和是奇数还是偶数得到不同的结果，原因在 PPT 第 2 张
    #     if (m + n) & 1:
    #         return max(nums1_left_max, nums2_left_max)
    #     else:
    #         return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2


# @lc code=end

