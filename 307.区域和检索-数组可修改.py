#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#

# @lc code=start
class FenwickTree(object):

    def __init__(self, n):
        self.sum = [0 for _ in range(n+1)]
        self.size = len(self.sum)

    def update(self, i, delta):
        while(i<self.size):
            self.sum[i] += delta
            i = i+self.lowbit(i)
    
    def get(self, i):
        ans = 0
        while(i>0):
            ans += self.sum[i]
            i = i-self.lowbit(i)
        return ans
    
    def lowbit(self, x):
        return x&(-x)

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ft = FenwickTree(len(nums))
        for i in range(len(nums)):
            self.ft.update(i+1, nums[i])
        

    def update(self, i: int, val: int) -> None:
        delta = val - self.nums[i]
        self.ft.update(i+1, delta)
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        a = self.ft.get(i)
        b = self.ft.get(j+1)
        return b-a

class SegmentTreeNode(object):
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val
        self.left = None
        self.right = None

class SegmentTree(object):
    def __init__(self, nums):
        self.nums= nums
        if self.nums:
            self.root = self.build_tree(0, len(nums)-1)

    def build_tree(self, start, end):
        if start==end:
            return SegmentTreeNode(start, end, self.nums[start]) 
        mid = (start+end)//2
        left = self.build_tree(start, mid)
        right = self.build_tree(mid+1, end)
        root = SegmentTreeNode(start, end, left.val+right.val)
        root.left, root.right = left, right
        return root 
    
    def query_range(self, root, start, end):
        if root.start == start and root.end == end:
            return root.val
        mid = (root.start+root.end)//2
        if mid<start:
            return self.query_range(root.right, start, end)
        elif mid>=end:
            return self.query_range(root.left, start, end) 
        else:
            left = self.query_range(root.left, start, mid)
            right = self.query_range(root.right, mid+1, end)
            return left+right

    def update(self, root, idx, val):
        if root.start == idx and root.end ==idx:
            root.val = val
            return
        mid = (root.start+root.end)//2
        if idx<=mid:
            self.update(root.left, idx, val)
        else:
            self.update(root.right, idx, val)
        root.val = root.left.val + root.right.val

        

class NumArray:

    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums)
        

    def update(self, i: int, val: int) -> None:
        root = self.st.root
        self.st.update(root, i, val)


    def sumRange(self, i: int, j: int) -> int:
        root = self.st.root
        print(root)
        return self.st.query_range(root, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end

