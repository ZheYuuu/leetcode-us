#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import List
import heapq
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
    
#     def __lt__(self, other):
#         if self.val<other.val:
#             return True
#         else:
#             return False
class Comparable:
    def __init__(self, val, node):
        self.val = val
        self.node = node
    
    def __lt__(self, other):
        return self.val<other.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # if not lists or (not lists[0] and len(lists)==1):
        #     return None
        head = pre = ListNode(-1)
        heap = [Comparable(node.val,node) for node in lists if node]
        heapq.heapify(heap)
        while(heap):
            c = heapq.heappop(heap)
            curr = c.node
            pre.next = curr
            if curr.next:
                heapq.heappush(heap, Comparable(curr.next.val, curr.next))
            pre = curr 
        return head.next


# if __name__ == "__main__":
#     heap = [ListNode(i) for i in range(10,-1,-1)]            
#     heapq.heapify(heap)
#     print(heap)



# @lc code=end

