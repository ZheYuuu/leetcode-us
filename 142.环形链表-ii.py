#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while(True):
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow==fast: break
        a = head
        b = fast
        while(a!=b):
            a = a.next
            b = b.next 
        return a 
# @lc code=end

