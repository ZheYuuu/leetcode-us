#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head 
        return self.partition(head)
    def partition(self, head):
        if not head.next:
            return head
        fast = head.next
        slow = head 
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        mid , slow.next = slow.next, None
        a = self.partition(head)
        b = self.partition(mid)
        return self.merge(a,b)

    def merge(self, a,b):
        dummy = curr = ListNode("dummy")
        while(a and b):
            if a.val<=b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next 
        curr.next = a if a else b
        return dummy.next
            


# @lc code=end

