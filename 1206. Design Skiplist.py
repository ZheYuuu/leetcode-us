import random


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None
        self.down = None
        self.cnt = 1


class Skiplist:

    def __init__(self):
        self.levels = [ListNode("dummy") for _ in range(16)]
        self.maxLevel = 16
        for i in reversed(range(1, 16)):
            self.levels[i].down = self.levels[i-1]

    def search(self, target: int) -> bool:
        cur = self.levels[-1]
        for i in reversed(range(self.maxLevel)):
            while(cur.next and cur.next.val <= target):
                cur = cur.next
            if cur.val == target:
                return True
            cur = cur.down
        return False

    def add(self, num: int) -> None:
        level = self.getRandomLevel(0.5)
        now = [ListNode(num) for _ in range(level)]
        for i in reversed(range(1, level)):
            now[i].down = now[i-1]

        cur = self.levels[-1]
        for i in reversed(range(self.maxLevel)):

            while(cur.next and cur.next.val <= num):
                cur = cur.next
            # duplicate element
            if cur.val == num:
                # if new duplicate element's level > original one's
                # add count  and connect
                if(i < level-1):
                    for j in range(i, level):
                        now[i].cnt += cur.cnt
                    now[i+1].down = cur
                while(cur):
                    cur.cnt += 1
                    cur = cur.down
                break
            # if i<level: insert one node into current layer
            if i < level:
                now[i].next = cur.next
                now[i].pre = cur
                if cur.next:
                    cur.next.pre = now[i]
                cur.next = now[i]

            # go down
            cur = cur.down

    def erase(self, num: int) -> bool:
        cur = self.levels[-1]
        flag = False
        for i in reversed(range(self.maxLevel)):
            while(cur.next and cur.next.val <= num):
                cur = cur.next
            if cur.val == num:
                if cur.cnt == 1:
                    pre = cur.pre
                    next = cur.next
                    pre.next = next
                    if next:
                        next.pre = pre
                else:
                    cur.cnt -= 1
                flag = True
            cur = cur.down
        return flag

    def getRandomLevel(self, p):
        level = 1
        while(random.random() < p and level < self.maxLevel):
            level += 1
        return level


if __name__ == "__main__":
    skiplist = Skiplist()
    ops = ["add","add","add","add","add","erase","erase","add","search","search","add","erase","search","add","add","add","erase","search","erase","search","search","search","erase","erase","search","erase","add","add","erase","add","search","search","search","search","search"]
    val = [[9],[4],[5],[6],[9],[2],[1],[2],[7],[4],[5],[6],[5],[6],[7],[4],[3],[6],[3],[4],[3],[8],[7],[6],[7],[4],[1],[6],[3],[4],[7],[6],[1],[0],[3]]
    for i in range(len(ops)):
        t = val[i]
        if ops[i]=="add":
            skiplist.add(t)
        elif ops[i] == "erase":
            skiplist.erase(t)
        elif ops[i] =="search":
            skiplist.search(t)
    

    # skiplist.add(1)
    # skiplist.search(0)
    # print(skiplist.erase(1))
    # skiplist.search(1)
# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
