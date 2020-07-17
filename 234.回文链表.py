#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True 
        slow, fast = head, head.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        if fast:
            dummy = ListNode("dummy")
            dummy.next = slow.next
            slow.next = dummy
            mid = dummy
        else:
            mid = slow
        tail = self.reverse(mid)
        while(tail!=head):
            if tail.val!=head.val:
                return False
            tail = tail.next
            head = head.next
        return True

        
    def reverse(self, head):
        pre,curr = None,head
        while(curr.next):
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        curr.next = pre
        return curr 

# def stringToListNode(numbers):
#     # Now convert that list into linked list
#     dummyRoot = ListNode(0)
#     ptr = dummyRoot
#     for number in numbers:
#         ptr.next = ListNode(number)
#         ptr = ptr.next

#     ptr = dummyRoot.next
#     return ptr


# if __name__ == "__main__":
        
#     line = [2,4,5,4,2]
#     head = stringToListNode(line)
#     res = Solution().isPalindrome(head)
#     print(res)
        
# @lc code=end

