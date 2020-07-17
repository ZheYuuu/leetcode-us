#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class MaxHeap:
    def __init__(self, arr):
        self.size = len(arr)
        self.heap = arr
        self.build()

    
    def heapify(self, i):
        if i>=self.size:
            return
        l = ll =self.left(i)
        r = rr = self.right(i)
        largest = i
        if l<self.size and self.heap[largest]<self.heap[l]:
            largest = l
        if r<self.size and self.heap[largest]<self.heap[r]:
            largest = r
        self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
        largest!=i and self.heapify(largest)
    
    def build(self):
        for i in reversed(range(self.size//2)):
            self.heapify(i)
    
    def heapsort(self, arr=None):
        if arr:
            self.heap, self.size = arr, len(arr)
            self.build()
        while(self.size):
            tail = self.size-1
            self.heap[tail], self.heap[0] = self.heap[0], self.heap[tail]
            self.size -= 1
            self.heapify(0)
        return self.heap
    
    def kthLargest(self, k):
        for i in range(k):
            tail = self.size-1
            self.heap[tail], self.heap[0] = self.heap[0], self.heap[tail]
            self.size -= 1
            self.heapify(0)
        return self.heap[-k]
            


    
    
    def left(self, i):
        return 2*i+1
    def right(self, i):
        return 2*i+2
    def parent(self, i):
        return (i-1)//2
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = MaxHeap(nums)
        return maxheap.kthLargest(k) 

# @lc code=end

