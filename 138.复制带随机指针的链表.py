#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        curr = head
        p= q = o =  Node(head.val, head.next)
        curr = curr.next
        lookup = {0:p}
        relookup = {head:0}
        idx = 0
        l = 1 
        while(curr):
            idx += 1
            l += 1
            node = Node(curr.val, curr.next)
            lookup[idx] = node
            relookup[curr] = idx
            p.next = node
            curr = curr.next 
            p = p.next
        lookup[l] = None
        curr = head
        while(curr):
            if not curr.random:
                idx = l
            else:
                idx = relookup[curr.random]
            q.random = lookup[idx]
            q = q.next
            curr  = curr.next
        return o
    
    def copyRandomList(self, head):
        if not head:
            return head
        d = dict()
        a = b = head
        while(a):
            d[a] = Node(a.val)
            a = a.next
        cnt = 0
        while(b):
            # when b.next or b.random is None, it fails because None cannot be key.
            # So use d.get
            d[b].next = d.get(b.next)
            d[b].random = d.get(b.random)
            b = b.next
        return d[head]

        


            
        
# @lc code=end

