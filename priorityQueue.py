import heapq
from itertools import count
REMOVED = '<removed-task>'

class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.entryFinder= {}
        self._counter = count()
    
    def addTask(self, task, priority=0):
        if task in self.entryFinder:
            self.remove_task(task)
        count = next(self._counter)
        entry = [priority, count, task]
        self.entryFinder[task] = entry
        heapq.heappush(self.pq, entry)

    def removeTask(self, task):
        entry = self.entryFinder[task]
        entry[-1] = REMOVED
    
    def popTask(self):
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not REMOVED:
                del self.entryFinder[task]
                return task
        raise KeyError("pop from an empty priority queue")