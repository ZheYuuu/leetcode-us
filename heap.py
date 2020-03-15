import heapq


class Camparable:
    def __init__(self, value, item):
        self.value = value
        self.item = item

    def __lt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"value: {self.value}, item: {self.item}"


l = [
    Camparable(1, "one"),
    Camparable(3, "three"),
    Camparable(4, "four"),
    Camparable(2, "two"),
]
heapq.heapify(l)
print(heapq.heappop(l))
class MaxHeap:
    def __init__(self, arr):
        self.size = len(arr)
        self.heap = arr

    
    def heapify(self, i):
        if i>=self.size:
            return
        l = ll =self.left(i)
        r = rr = self.right(i)
        largest = i
        if l<self.size and self.heap[largest]<self.heap[l]:
            largest = l
        if r<self.size and self.heap[largest]<self.heap[r]:
            largest = r
        self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
        largest!=i and self.heapify(largest)
    
    def build(self):
        for i in reversed(range(self.size//2)):
            self.heapify(i)
    
    def heapsort(self, arr=None):
        if arr:
            self.heap, self.size = arr, len(arr)
            self.build()
        while(self.size):
            tail = self.size-1
            self.heap[tail], self.heap[0] = self.heap[0], self.heap[tail]
            self.size -= 1
            self.heapify(0)
        return self.heap

    
    
    def left(self, i):
        return 2*i+1
    def right(self, i):
        return 2*i+2
    def parent(self, i):
        return (i-1)//2

if __name__ == "__main__":
    arr = [23,17,14,6,13,10,1,5,7,12]
    maxHeap = MaxHeap(arr)
    maxHeap.build()
    print("ans:",maxHeap.heapsort())
    