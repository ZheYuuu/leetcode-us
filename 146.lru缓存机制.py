#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
class Node:
    def __init__(self, key=None, val=None, **kwargs):
        self.pre = None
        self.next = None
        self.key = key
        self.val = val


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        if key in self.mapping:
            self.moveToHead(key)
        return self.mapping[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.moveToHead(key)
            node = self.mapping[key]
            node.val = value
        else:
            if len(self.mapping) == self.capacity:
                tmp = self.tail.pre
                self.mapping.pop(tmp.key)
                tmp.pre.next = self.tail
                self.tail.pre = tmp.pre
            node = Node(key, value)
            tmp = self.head.next
            self.head.next = node
            node.pre = self.head

            node.next = tmp
            tmp.pre = node

            self.mapping[key] = node


    
    def moveToHead(self, key):
        node = self.mapping[key]
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node



if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(2, 1)
    lru.put(2, 2)
    print("get:", lru.get(2))
    lru.put(3, 3)
    lru.get(2)
    lru.put(4, 4)
    lru.put(4,8)
    print("get:", lru.get(1))
    print("get:", lru.get(3))
    print("get:", lru.get(4))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

