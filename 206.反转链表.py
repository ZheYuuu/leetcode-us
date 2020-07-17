#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None 
        curr = head
        while(curr):
            nextTmp = curr.next
            curr.next = pre
            pre = curr
            curr = nextTmp
        return pre 
            


         
        
# @lc code=end

