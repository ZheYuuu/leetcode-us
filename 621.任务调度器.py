#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
from typing import List
from collections import Counter
import heapq
from itertools import count
import collections

REMOVED = "<removed-task>"


class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.entryFinder = {}
        self._counter = count()
        self.size = 0

    def addTask(self, task, priority=0):
        if task in self.entryFinder and self.entryFinder[task][-1] != REMOVED:
            self.remove_task(task)
        count = next(self._counter)
        entry = [priority, count, task]
        self.entryFinder[task] = entry
        self.size += 1
        heapq.heappush(self.pq, entry)

    def removeTask(self, task):
        self.size -= 1
        entry = self.entryFinder[task]
        entry[-1] = REMOVED

    def popTask(self):
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not REMOVED:
                self.size -= 1
                del self.entryFinder[task]
                return task, priority
        raise KeyError("pop from an empty priority queue")

    def findMin(self):
        while self.pq:
            if self.pq[0][-1] == REMOVED:
                heapq.heappop(self.pq)
            else:
                return self.pq[0][-1], self.pq[0][0]
        raise KeyError("The priority queue is empty")

    @property
    def isEmpty(self):
        return self.size == 0
    
    def __repr__(self):
        s = [f"{i[2]}:{i[0]}" for i in self.pq]
        return ",".join(s)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        hm = {}
        t = 0
        for task in tasks:
            hm[task] = hm.get(task, 0) + 1
            t = max(t, hm[task])
        print(hm)
        counts = sorted(hm.values(), reverse=True)

        ret = 0
        while counts:
            if len(counts) - 1 >= n:
                t = counts.pop(-1)
                ret += t * (len(counts))
                _counts = []
                for i in range(len(counts)):
                    counts[i] -= t
                    if counts[i] > 0:
                        _counts.append(counts[i])
                counts = _counts
            else:
                i = 0
                while i < len(counts) - 1:
                    if counts[i] == counts[i + 1]:
                        i = i + 1
                    else:
                        break
                ret += (counts[0] - 1) * (n + 1) + i + 1
                break
        return ret

    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = PriorityQueue()
        counts = collections.Counter(tasks)
        for key, val in counts.items():
            pq.addTask(key, -val)
        count= 0
        while not pq.isEmpty:
            # print(pq)
            interval = n + 1
            _pq = []
            while interval > 0 and not pq.isEmpty:
                task, cnt = pq.popTask()
                if task==REMOVED:
                    continue
                _pq.append([task, cnt + 1])
                interval -= 1
                count += 1
            for task, cnt in _pq:
                if cnt < 0:
                    pq.addTask(task, cnt)
            if pq.isEmpty:
                break
            # print(f"interval:{interval}, cnt:{cnt}")
            count += interval
        return count 


# if __name__ == "__main__":
#     sol = Solution()
#     t = sol.leastInterval( ["A","A","A","B","B","B"],
#         0,
#     )
#     print(t)


# @lc code=end

